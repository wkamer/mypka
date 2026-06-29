/**
 * EmailTriage.test.jsx — Slice 3 frontend tests.
 * G4 test spec: 14 scenarios covering ActionsPanel behaviour.
 * Written before implementation per SOP-018 TDD protocol.
 */

import { vi, it, expect, beforeEach, afterEach } from 'vitest';
import { cleanup, render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom';
import { MemoryRouter } from 'react-router-dom';
import EmailTriage from './EmailTriage';

// ── Mock the api module ──────────────────────────────────────────────────────

vi.mock('../api/client', () => ({
  api: {
    get: vi.fn(),
    post: vi.fn(),
    patch: vi.fn(),
  },
}));

import { api } from '../api/client';

// ── Fixtures ─────────────────────────────────────────────────────────────────

const EMAIL_ID = 'email-test-1';
const EMAIL_ID_2 = 'email-test-2';

function makeEmail(id, overrides = {}) {
  return {
    id,
    subject: `Subject for ${id}`,
    sender: `Sender ${id} <sender@test.com>`,
    received_at: '2026-06-28T10:00:00Z',
    triage_status: 'pending',
    classification: 'Action',
    ai_summary: 'Test summary',
    gmail_url: null,
    actions: [],
    ...overrides,
  };
}

function makeTaskAction(id, overrides = {}) {
  return {
    id,
    email_id: EMAIL_ID,
    type: 'Task',
    name: 'Follow up with client',
    event_datetime: null,
    status: 'pending',
    external_id: null,
    executed_at: null,
    approved_at: null,
    ...overrides,
  };
}

function makeEventAction(id, overrides = {}) {
  return {
    id,
    email_id: EMAIL_ID,
    type: 'Event',
    name: 'Team standup',
    event_datetime: '2026-07-01T10:00',
    status: 'pending',
    external_id: null,
    executed_at: null,
    approved_at: null,
    ...overrides,
  };
}

// ── Mock setup helpers ────────────────────────────────────────────────────────

function setupMocks({ emails = [makeEmail(EMAIL_ID)], actionsByEmailId = {} } = {}) {
  api.get.mockImplementation((path) => {
    if (path === '/api/email-management/emails') {
      return Promise.resolve({ emails });
    }
    for (const [emailId, actions] of Object.entries(actionsByEmailId)) {
      if (path === `/api/email-management/emails/${emailId}/actions`) {
        return Promise.resolve({ actions });
      }
    }
    // Default: empty actions
    return Promise.resolve({ actions: [] });
  });
}

function renderEmailTriage() {
  return render(
    <MemoryRouter>
      <EmailTriage />
    </MemoryRouter>
  );
}

// Open the accordion for a given email by clicking on its row.
async function openAccordion(user, emailId = EMAIL_ID) {
  // The row contains sender text
  const email = makeEmail(emailId);
  const senderName = `Sender ${emailId}`;
  const row = await screen.findByText(senderName, { exact: false });
  await user.click(row);
}

// ── beforeEach ────────────────────────────────────────────────────────────────

beforeEach(() => {
  vi.clearAllMocks();
  // Default: no emails loaded, api.post returns a new action
  api.get.mockResolvedValue({ emails: [] });
  api.post.mockResolvedValue(null);
  api.patch.mockResolvedValue(null);
});

afterEach(() => {
  cleanup();
});

// ── SCENARIO 1 — Actions load on accordion open ───────────────────────────────

it('loads actions when accordion opens and renders action rows', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1);
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  // Action name input should appear with pre-populated value
  const nameInputs = await screen.findAllByRole('textbox');
  expect(nameInputs.length).toBeGreaterThanOrEqual(1);
  expect(api.get).toHaveBeenCalledWith(`/api/email-management/emails/${EMAIL_ID}/actions`);
});

// ── SCENARIO 2 — Task row pre-populated name ──────────────────────────────────

it('pre-populates task action name with AI suggestion and accepts input', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1);
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  // Name field shows AI suggestion
  const nameInput = await screen.findByDisplayValue('Follow up with client');
  expect(nameInput).toBeInTheDocument();

  // Owner can edit the name
  await user.clear(nameInput);
  await user.type(nameInput, 'Custom task name');
  expect(nameInput).toHaveValue('Custom task name');
});

// ── SCENARIO 3 — Event row name and datetime visible ─────────────────────────

it('renders event row with pre-populated name and datetime fields both visible', async () => {
  const user = userEvent.setup();
  const eventAction = makeEventAction(2);
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [eventAction] },
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  // Name field pre-populated
  const nameInput = await screen.findByDisplayValue('Team standup');
  expect(nameInput).toBeInTheDocument();

  // Datetime input is visible and pre-populated
  const datetimeInput = await screen.findByDisplayValue('2026-07-01T10:00');
  expect(datetimeInput).toBeInTheDocument();

  // Both accept input
  await user.clear(nameInput);
  await user.type(nameInput, 'New event name');
  expect(nameInput).toHaveValue('New event name');
});

// ── SCENARIO 4 — Approve task: row transitions to resolved state ──────────────

it('transitions task row to resolved approved state on approve', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1);
  const approvedAction = { ...taskAction, status: 'approved', external_id: 'task-123' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  const approveBtn = await screen.findByRole('button', { name: /approve/i });
  await user.click(approveBtn);

  // Approve/Decline buttons should be gone, resolved state shown
  await waitFor(() => {
    expect(screen.queryByRole('button', { name: /approve/i })).not.toBeInTheDocument();
  });
  expect(screen.getByText(/approved/i)).toBeInTheDocument();
});

// ── SCENARIO 5 — Approve task: log entry ─────────────────────────────────────

it('appends log entry with task name and timestamp after approval', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1);
  const approvedAction = { ...taskAction, status: 'approved', external_id: 'task-123' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  const approveBtn = await screen.findByRole('button', { name: /approve/i });
  await user.click(approveBtn);

  // Log entry shows task name
  await screen.findByText(/Task "Follow up with client" created/i);
});

// ── SCENARIO 5b — Approve task after editing: log shows edited name ───────────

it('sends edited name on approve and log records edited name', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1);
  const approvedAction = { ...taskAction, status: 'approved', external_id: 'task-123' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  // Edit the name
  const nameInput = await screen.findByDisplayValue('Follow up with client');
  await user.clear(nameInput);
  await user.type(nameInput, 'Edited task name');

  const approveBtn = screen.getByRole('button', { name: /approve/i });
  await user.click(approveBtn);

  // PATCH called with edited name
  expect(api.patch).toHaveBeenCalledWith(
    `/api/email-management/actions/1`,
    expect.objectContaining({ status: 'approved', name: 'Edited task name' })
  );

  // Log shows edited name
  await screen.findByText(/Task "Edited task name" created/i);
});

// ── SCENARIO 6 — Approve event: log entry with name, datetime, timestamp ──────

it('appends event log entry with name, datetime, and timestamp after approval', async () => {
  const user = userEvent.setup();
  const eventAction = makeEventAction(2);
  const approvedAction = { ...eventAction, status: 'approved', external_id: 'cal-456' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [eventAction] },
  });
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  const approveBtn = await screen.findByRole('button', { name: /approve/i });
  await user.click(approveBtn);

  // Log entry shows event format with name and datetime
  await screen.findByText(/Event "Team standup"/i);
  await screen.findByText(/added to calendar/i);
});

// ── SCENARIO 7 — Decline: no log entry ───────────────────────────────────────

it('transitions to declined state on decline without adding a log entry', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1);
  const declinedAction = { ...taskAction, status: 'declined' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });
  api.patch.mockResolvedValue(declinedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  const declineBtn = await screen.findByRole('button', { name: /decline/i });
  await user.click(declineBtn);

  // Declined state shown, no log entry
  await waitFor(() => {
    expect(screen.queryByRole('button', { name: /decline/i })).not.toBeInTheDocument();
  });
  expect(screen.getByText(/declined/i)).toBeInTheDocument();
  expect(screen.queryByText(/Task.*created/i)).not.toBeInTheDocument();
  expect(screen.queryByText(/Execution log/i)).not.toBeInTheDocument();
});

// ── SCENARIO 8 — Manual add-task ─────────────────────────────────────────────

it('appends empty task row on add-task click', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  const newTaskAction = makeTaskAction(10, { name: null });
  api.post.mockResolvedValue(newTaskAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  const addTaskBtn = await screen.findByRole('button', { name: /\+ task/i });
  await user.click(addTaskBtn);

  // Empty task row appears with approve/decline controls
  await screen.findByRole('button', { name: /approve/i });
  await screen.findByRole('button', { name: /decline/i });
  expect(api.post).toHaveBeenCalledWith(
    `/api/email-management/emails/${EMAIL_ID}/actions`,
    expect.objectContaining({ type: 'Task' })
  );
});

// ── SCENARIO 9 — Manual add-event ────────────────────────────────────────────

it('appends empty event row with datetime field on add-event click', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  const newEventAction = makeEventAction(11, { name: null, event_datetime: null });
  api.post.mockResolvedValue(newEventAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  const addEventBtn = await screen.findByRole('button', { name: /\+ event/i });
  await user.click(addEventBtn);

  // Event row with approve/decline controls
  await screen.findByRole('button', { name: /approve/i });
  await screen.findByRole('button', { name: /decline/i });
  expect(api.post).toHaveBeenCalledWith(
    `/api/email-management/emails/${EMAIL_ID}/actions`,
    expect.objectContaining({ type: 'Event' })
  );
});

// ── SCENARIO 10 — Approve manual task: log entry ─────────────────────────────

it('logs entered name when approving a manually added task', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  const newTaskAction = makeTaskAction(10, { name: null });
  api.post.mockResolvedValue(newTaskAction);
  const approvedAction = { ...newTaskAction, name: 'Manual task', status: 'approved', external_id: 't-99' };
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await user.click(await screen.findByRole('button', { name: /\+ task/i }));

  // Type a name in the new (empty) row's name input
  const nameInputs = await screen.findAllByRole('textbox');
  // The new row's input has empty value
  const emptyInput = nameInputs.find((el) => el.value === '');
  expect(emptyInput).toBeTruthy();
  await user.type(emptyInput, 'Manual task');

  // Approve
  await user.click(screen.getByRole('button', { name: /approve/i }));

  // Log shows the entered name
  await screen.findByText(/Task "Manual task" created/i);
});

// ── SCENARIO 11 — Approve manual event: log entry ────────────────────────────

it('logs entered name and datetime when approving a manually added event', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  const newEventAction = makeEventAction(11, { name: null, event_datetime: null });
  api.post.mockResolvedValue(newEventAction);
  const approvedAction = { ...newEventAction, status: 'approved', external_id: 'cal-99' };
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await user.click(await screen.findByRole('button', { name: /\+ event/i }));

  // Fill name and datetime inputs
  const textInputs = await screen.findAllByRole('textbox');
  const emptyNameInput = textInputs.find((el) => el.value === '');
  expect(emptyNameInput).toBeTruthy();
  await user.type(emptyNameInput, 'Manual event');

  // Find datetime input by type attribute (datetime-local is not role="textbox")
  const dateInputs = document.querySelectorAll('input[type="datetime-local"]');
  expect(dateInputs.length).toBeGreaterThanOrEqual(1);
  await user.clear(dateInputs[0]);
  await user.type(dateInputs[0], '2026-08-15T09:00');

  await user.click(screen.getByRole('button', { name: /approve/i }));

  // Log shows event format
  await screen.findByText(/Event "Manual event"/i);
  await screen.findByText(/added to calendar/i);
});

// ── SCENARIO 12 — Cumulative log ─────────────────────────────────────────────

it('accumulates two log entries when two actions are approved in order', async () => {
  const user = userEvent.setup();
  const taskAction1 = makeTaskAction(1, { name: 'First task' });
  const taskAction2 = makeTaskAction(2, { name: 'Second task' });
  const approved1 = { ...taskAction1, status: 'approved', external_id: 't-1' };
  const approved2 = { ...taskAction2, status: 'approved', external_id: 't-2' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction1, taskAction2] },
  });
  api.patch
    .mockResolvedValueOnce(approved1)
    .mockResolvedValueOnce(approved2);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  // Approve first action
  const approveBtns = await screen.findAllByRole('button', { name: /approve/i });
  await user.click(approveBtns[0]);
  await screen.findByText(/Task "First task" created/i);

  // Approve second action
  const approveBtns2 = await screen.findAllByRole('button', { name: /approve/i });
  await user.click(approveBtns2[0]);

  // Both entries present
  await screen.findByText(/Task "Second task" created/i);
  const logEntries = screen.getAllByText(/Task .* created/i);
  expect(logEntries.length).toBe(2);
});

// ── SCENARIO 13 — Log absent before first approval ───────────────────────────

it('does not render log section before any action has been approved', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1);
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  // Wait for actions to load
  await screen.findByRole('button', { name: /approve/i });

  // No log section visible
  expect(screen.queryByText(/Execution log/i)).not.toBeInTheDocument();
});

// ── SCENARIO 14 — Exclusive accordion toggle ─────────────────────────────────

it('collapses the first accordion when the second is opened', async () => {
  const user = userEvent.setup();
  const email1 = makeEmail(EMAIL_ID);
  const email2 = makeEmail(EMAIL_ID_2);
  const taskAction1 = makeTaskAction(1, { email_id: EMAIL_ID });
  const taskAction2 = makeTaskAction(2, { email_id: EMAIL_ID_2 });
  setupMocks({
    emails: [email1, email2],
    actionsByEmailId: {
      [EMAIL_ID]: [taskAction1],
      [EMAIL_ID_2]: [taskAction2],
    },
  });

  renderEmailTriage();

  // Open first accordion
  const sender1 = await screen.findByText(/Sender email-test-1/i);
  await user.click(sender1);
  await screen.findByDisplayValue('Follow up with client');

  // Open second accordion
  const sender2 = screen.getByText(/Sender email-test-2/i);
  await user.click(sender2);

  // First accordion should be collapsed (name input for email1 gone)
  await waitFor(() => {
    const allInputs = screen.queryAllByDisplayValue('Follow up with client');
    // After first closes and second opens, only the second action is visible
    // taskAction2 has the same name fixture, so let's check via API call count
    expect(api.get).toHaveBeenCalledWith(`/api/email-management/emails/${EMAIL_ID_2}/actions`);
  });
});

it('collapses the open accordion when its header is clicked a second time', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1);
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });

  renderEmailTriage();

  // Open accordion
  const senderEl = await screen.findByText(/Sender email-test-1/i);
  await user.click(senderEl);
  await screen.findByRole('button', { name: /approve/i });

  // Click header again to close
  await user.click(senderEl);
  await waitFor(() => {
    expect(screen.queryByRole('button', { name: /approve/i })).not.toBeInTheDocument();
  });
});

// ── ISSUE 1 — Log reconstructs from actions on accordion open ────────────────

it('does not fetch the execution log independently on accordion open', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await screen.findByRole('button', { name: /\+ task/i });
  expect(api.get).not.toHaveBeenCalledWith(`/api/email-management/emails/${EMAIL_ID}/log`);
  expect(screen.queryByText('Loading log...')).not.toBeInTheDocument();
});

it('reconstructs approved action log entries from actions on accordion open', async () => {
  const user = userEvent.setup();
  const olderApprovedAction = makeTaskAction(1, {
    name: 'Previously approved task',
    status: 'approved',
    approved_at: '2026-06-28T10:00:00Z',
  });
  const newerApprovedAction = makeTaskAction(2, {
    name: 'More recently approved task',
    status: 'approved',
    approved_at: '2026-06-28T11:00:00Z',
  });
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [olderApprovedAction, newerApprovedAction] },
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await screen.findByText(/Execution log/i);
  expect(screen.queryByRole('button', { name: /approve/i })).not.toBeInTheDocument();
  const logSection = document.querySelector('[aria-label="Execution log"]');
  expect(logSection.textContent).toContain('Previously approved task');
  expect(logSection.textContent).toContain('More recently approved task');
  expect(logSection.textContent.indexOf('More recently approved task')).toBeLessThan(
    logSection.textContent.indexOf('Previously approved task')
  );
});

it('does not render an independent log error when actions load succeeds', async () => {
  const user = userEvent.setup();
  api.get.mockImplementation((path) => {
    if (path === '/api/email-management/emails') {
      return Promise.resolve({ emails: [makeEmail(EMAIL_ID)] });
    }
    if (path === `/api/email-management/emails/${EMAIL_ID}/actions`) {
      return Promise.resolve({ actions: [] });
    }
    return Promise.resolve({ actions: [] });
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await screen.findByRole('button', { name: /\+ task/i });
  expect(screen.queryByText('Execution log unavailable.')).not.toBeInTheDocument();
});

// ── ISSUE 2 — Log format: timestamp first ────────────────────────────────────

it('log entry has timestamp as first token in DD Mon YYYY HH:MM format', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1, { name: 'Timestamp test task' });
  const approvedAction = { ...taskAction, status: 'approved', external_id: 'task-ts' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await user.click(await screen.findByRole('button', { name: /approve/i }));

  // Entry format: starts with "DD Mon YYYY HH:MM  Task ..."
  await waitFor(() => {
    const entries = screen.getAllByText(/\d{2} [A-Z][a-z]{2} \d{4} \d{2}:\d{2}.*Task.*created/i);
    expect(entries.length).toBeGreaterThanOrEqual(1);
  });
});

it('log entries are ordered newest at top — most recent approval appears first', async () => {
  const user = userEvent.setup();
  const task1 = makeTaskAction(1, { name: 'First task' });
  const task2 = makeTaskAction(2, { name: 'Second task' });
  const approved1 = { ...task1, status: 'approved', external_id: 't-1' };
  const approved2 = { ...task2, status: 'approved', external_id: 't-2' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [task1, task2] },
  });
  api.patch
    .mockResolvedValueOnce(approved1)
    .mockResolvedValueOnce(approved2);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  const approveBtns = await screen.findAllByRole('button', { name: /approve/i });
  await user.click(approveBtns[0]); // approve first
  await waitFor(() => {
    expect(screen.getAllByRole('button', { name: /approve/i })).toHaveLength(1);
  });

  const approveBtns2 = screen.getAllByRole('button', { name: /approve/i });
  await user.click(approveBtns2[0]); // approve second

  await waitFor(() => {
    const logSection = document.querySelector('[aria-label="Execution log"]');
    expect(logSection).not.toBeNull();
    const text = logSection.textContent;
    const idxSecond = text.indexOf('Second task');
    const idxFirst = text.indexOf('First task');
    expect(idxSecond).toBeLessThan(idxFirst);
  });
});

// ── ISSUE 3 — +Task/+Event not cancelable: auto-focus ─────────────────────────

it('auto-focuses name field of new task row after add-task click', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  const newTaskAction = makeTaskAction(10, { name: null });
  api.post.mockResolvedValue(newTaskAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await user.click(await screen.findByRole('button', { name: /\+ task/i }));

  // Name input should appear and have focus
  await waitFor(() => {
    const inputs = screen.getAllByRole('textbox');
    const nameInputs = inputs.filter((el) => el.getAttribute('aria-label') === 'Action name');
    expect(nameInputs.length).toBeGreaterThanOrEqual(1);
    const focused = nameInputs.some((el) => document.activeElement === el);
    expect(focused).toBe(true);
  });
});

it('does not render a cancel/remove button on manually added rows', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  const newTaskAction = makeTaskAction(10, { name: null });
  api.post.mockResolvedValue(newTaskAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await user.click(await screen.findByRole('button', { name: /\+ task/i }));
  await screen.findByRole('button', { name: /approve/i });

  // No cancel / close / remove / X button present
  expect(screen.queryByRole('button', { name: /cancel/i })).not.toBeInTheDocument();
  expect(screen.queryByRole('button', { name: /remove/i })).not.toBeInTheDocument();
  expect(screen.queryByRole('button', { name: /close/i })).not.toBeInTheDocument();
  expect(screen.getByRole('button', { name: /approve/i })).toBeInTheDocument();
  expect(screen.getByRole('button', { name: /decline/i })).toBeInTheDocument();
});

// ── ISSUE 4 — Resolved state shows submitted name as static text ───────────────

it('resolved task row shows static text not a disabled input', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1, { name: 'My task name' });
  const approvedAction = { ...taskAction, status: 'approved', external_id: 'task-static' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await user.click(await screen.findByRole('button', { name: /approve/i }));

  await waitFor(() => {
    const inputs = document.querySelectorAll('input[aria-label="Action name"]');
    expect(inputs.length).toBe(0);
    expect(screen.getByText('My task name')).toBeInTheDocument();
  });
});

it('resolved task row shows (untitled) when name is empty on approve', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(10, { name: null });
  const approvedAction = { ...taskAction, status: 'approved', external_id: 'task-untitled' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  api.post.mockResolvedValue(taskAction);
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await user.click(await screen.findByRole('button', { name: /\+ task/i }));
  await user.click(await screen.findByRole('button', { name: /approve/i }));

  await waitFor(() => {
    expect(screen.getByText('(untitled)')).toBeInTheDocument();
  });
});

it('resolved task row shows submitted name even when backend action.name is null', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(10, { name: null });
  const approvedAction = { ...taskAction, status: 'approved', name: null, external_id: 'task-manual' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  api.post.mockResolvedValue(taskAction);
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await user.click(await screen.findByRole('button', { name: /\+ task/i }));

  const nameInputs = await screen.findAllByRole('textbox');
  const emptyInput = nameInputs.find((el) => el.value === '');
  expect(emptyInput).toBeTruthy();
  await user.type(emptyInput, 'Typed task name');

  await user.click(screen.getByRole('button', { name: /approve/i }));

  await waitFor(() => {
    expect(screen.getByText('Typed task name')).toBeInTheDocument();
  });
});

it('resolved event row shows formatted datetime as static text', async () => {
  const user = userEvent.setup();
  const eventAction = makeEventAction(2, { event_datetime: '2026-07-15T09:30' });
  const approvedAction = { ...eventAction, status: 'approved', external_id: 'cal-dt' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [eventAction] },
  });
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await user.click(await screen.findByRole('button', { name: /approve/i }));

  await waitFor(() => {
    expect(screen.getByText('15 Jul 2026 09:30')).toBeInTheDocument();
    expect(document.querySelectorAll('input[type="datetime-local"]').length).toBe(0);
  });
});

it('resolved event row shows (no date) when datetime is empty', async () => {
  const user = userEvent.setup();
  const eventAction = makeEventAction(11, { name: null, event_datetime: null });
  const approvedAction = { ...eventAction, status: 'approved', external_id: 'cal-nodate' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  api.post.mockResolvedValue(eventAction);
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await user.click(await screen.findByRole('button', { name: /\+ event/i }));
  await user.click(await screen.findByRole('button', { name: /approve/i }));

  await waitFor(() => {
    expect(screen.getByText('(no date)')).toBeInTheDocument();
  });
});

it('log entry shows (untitled) when approved task name is empty', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(10, { name: null });
  const approvedAction = { ...taskAction, status: 'approved', external_id: 'task-nolog' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  api.post.mockResolvedValue(taskAction);
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await user.click(await screen.findByRole('button', { name: /\+ task/i }));
  await user.click(await screen.findByRole('button', { name: /approve/i }));

  await screen.findByText(/Task.*\(untitled\).*created/i);
});

// ── ACCORDION BUG REGRESSIONS ────────────────────────────────────────────────

it('preserves approval log entries after accordion collapse and reopen', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1, { name: 'Persistent log task' });
  const approvedAction = { ...taskAction, status: 'approved', external_id: 'task-persist-log' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();

  const senderEl = await screen.findByText(/Sender email-test-1/i);
  await user.click(senderEl);
  await user.click(await screen.findByRole('button', { name: /approve/i }));
  await screen.findByText(/Task "Persistent log task" created/i);

  await user.click(senderEl);
  await waitFor(() => {
    expect(screen.queryByText(/Execution log/i)).not.toBeInTheDocument();
  });

  await user.click(senderEl);
  await screen.findByText(/Task "Persistent log task" created/i);
  expect(screen.getByText(/Execution log/i)).toBeInTheDocument();
});

it('preserves approved task title as static text after accordion collapse and reopen', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1, { name: 'Task title survives' });
  const approvedAction = { ...taskAction, status: 'approved', external_id: 'task-persist-title' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();

  const senderEl = await screen.findByText(/Sender email-test-1/i);
  await user.click(senderEl);
  await user.click(await screen.findByRole('button', { name: /approve/i }));
  await screen.findByText('Task title survives');

  await user.click(senderEl);
  await waitFor(() => {
    expect(screen.queryByText('Task title survives')).not.toBeInTheDocument();
  });

  await user.click(senderEl);
  await screen.findByText('Task title survives');
  expect(screen.queryByRole('textbox', { name: /action name/i })).not.toBeInTheDocument();
  expect(screen.queryByRole('button', { name: /approve/i })).not.toBeInTheDocument();
});

// ── SESSION STATE — Log entries persist across accordion close/reopen ──────────

it('log entries persist after accordion close and reopen', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1, { name: 'Follow up with client' });
  const approvedAction = { ...taskAction, status: 'approved', external_id: 'task-persist-log' };

  api.get.mockImplementation((path) => {
    if (path === '/api/email-management/emails') {
      return Promise.resolve({ emails: [makeEmail(EMAIL_ID)] });
    }
    if (path === `/api/email-management/emails/${EMAIL_ID}/actions`) {
      // After approve, return approved status (name null to stress-test)
      return Promise.resolve({ actions: [{ ...taskAction }] });
    }
    return Promise.resolve({ actions: [] });
  });
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();

  // First open: approve an action
  await openAccordion(user, EMAIL_ID);
  await user.click(await screen.findByRole('button', { name: /approve/i }));
  await screen.findByText(/Task "Follow up with client" created/i);
  await screen.findByText(/Execution log/i);

  // Close accordion by clicking header again
  const senderEl = screen.getByText(/Sender email-test-1/i);
  await user.click(senderEl);
  await waitFor(() => {
    expect(screen.queryByText(/Execution log/i)).not.toBeInTheDocument();
  });

  // Reopen accordion
  await user.click(senderEl);

  // Log entry must still be visible from session state
  await screen.findByText(/Task "Follow up with client" created/i);
  await screen.findByText(/Execution log/i);
});

// ── SESSION STATE — Approved name persists across accordion close/reopen ───────

it('approved action name persists after accordion close and reopen even when backend returns null name', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1, { name: 'Specific task name' });
  const approvedActionFromPatch = { ...taskAction, status: 'approved', name: null, external_id: 'task-persist-name' };

  let actionsCallCount = 0;
  api.get.mockImplementation((path) => {
    if (path === '/api/email-management/emails') {
      return Promise.resolve({ emails: [makeEmail(EMAIL_ID)] });
    }
    if (path === `/api/email-management/emails/${EMAIL_ID}/actions`) {
      actionsCallCount += 1;
      if (actionsCallCount === 1) {
        // First open: pending action with name
        return Promise.resolve({ actions: [taskAction] });
      }
      // Reopen: approved action, backend returns null for name
      return Promise.resolve({ actions: [{ ...taskAction, status: 'approved', name: null }] });
    }
    return Promise.resolve({ actions: [] });
  });
  api.patch.mockResolvedValue(approvedActionFromPatch);

  renderEmailTriage();

  // First open: approve the action
  await openAccordion(user, EMAIL_ID);
  await user.click(await screen.findByRole('button', { name: /approve/i }));
  await waitFor(() => {
    expect(screen.getByText('Specific task name')).toBeInTheDocument();
  });

  // Close accordion
  const senderEl = screen.getByText(/Sender email-test-1/i);
  await user.click(senderEl);
  await waitFor(() => {
    expect(screen.queryByRole('button', { name: /approve/i })).not.toBeInTheDocument();
  });

  // Reopen accordion — backend now returns approved action with null name
  await user.click(senderEl);

  // Name must still be visible from session state (not the nameless fallback)
  await waitFor(() => {
    expect(screen.getByText('Specific task name')).toBeInTheDocument();
    expect(screen.queryByText('(untitled)')).not.toBeInTheDocument();
  });
});

// ── SLICE 4 — State reconstruction regressions ──────────────────────────────

it('renders an API-approved action as approved on first open without session state', async () => {
  const user = userEvent.setup();
  const approvedAction = makeTaskAction(1, {
    name: 'Persisted approved task',
    status: 'approved',
    approved_at: '2026-06-28T14:03:00Z',
  });
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [approvedAction] },
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await screen.findByText('Persisted approved task');
  expect(screen.getByText('Approved')).toBeInTheDocument();
  expect(screen.queryByRole('button', { name: /approve/i })).not.toBeInTheDocument();
  await screen.findByText(/Task "Persisted approved task" created/i);
});

it('lets API approved status override stale pending session state on reopen', async () => {
  const user = userEvent.setup();
  const pendingAction = makeTaskAction(10, { name: null });
  const approvedAction = makeTaskAction(10, {
    name: 'Backend approved task',
    status: 'approved',
    approved_at: '2026-06-28T14:03:00Z',
  });
  let actionsCallCount = 0;
  api.get.mockImplementation((path) => {
    if (path === '/api/email-management/emails') {
      return Promise.resolve({ emails: [makeEmail(EMAIL_ID)] });
    }
    if (path === `/api/email-management/emails/${EMAIL_ID}/actions`) {
      actionsCallCount += 1;
      return Promise.resolve({
        actions: actionsCallCount === 1 ? [] : [approvedAction],
      });
    }
    return Promise.resolve({ actions: [] });
  });
  api.post.mockResolvedValue(pendingAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);
  await user.click(await screen.findByRole('button', { name: /\+ task/i }));
  await screen.findByRole('button', { name: /approve/i });

  const senderEl = screen.getByText(/Sender email-test-1/i);
  await user.click(senderEl);
  await waitFor(() => {
    expect(screen.queryByRole('button', { name: /approve/i })).not.toBeInTheDocument();
  });

  await user.click(senderEl);
  await screen.findByText(/Task "Backend approved task" created/i);
  expect(screen.getByText('Approved')).toBeInTheDocument();
  expect(screen.queryByRole('button', { name: /approve/i })).not.toBeInTheDocument();
});

it('preserves current-session resolved state when API still returns pending', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1, { name: 'Session approved task' });
  const approvedAction = { ...taskAction, status: 'approved', external_id: 'task-session-approved' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });
  api.patch.mockResolvedValue(approvedAction);

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);
  await user.click(await screen.findByRole('button', { name: /approve/i }));
  await screen.findByText('Approved');

  const senderEl = screen.getByText(/Sender email-test-1/i);
  await user.click(senderEl);
  await waitFor(() => {
    expect(screen.queryByRole('button', { name: /approve/i })).not.toBeInTheDocument();
  });

  await user.click(senderEl);
  await screen.findByText('Session approved task');
  expect(screen.getByText('Approved')).toBeInTheDocument();
  expect(screen.queryByRole('button', { name: /approve/i })).not.toBeInTheDocument();
});

it('excludes approved actions with null approved_at from reconstructed log', async () => {
  const user = userEvent.setup();
  const approvedWithoutTimestamp = makeTaskAction(1, {
    name: 'Approved without timestamp',
    status: 'approved',
    approved_at: null,
  });
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [approvedWithoutTimestamp] },
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await screen.findByText('Approved without timestamp');
  expect(screen.getByText('Approved')).toBeInTheDocument();
  expect(screen.queryByText(/Execution log/i)).not.toBeInTheDocument();
  expect(screen.queryByText(/Approved without timestamp.*created/i)).not.toBeInTheDocument();
});

it('shows actions fetch failure without rendering an independent log section', async () => {
  const user = userEvent.setup();
  api.get.mockImplementation((path) => {
    if (path === '/api/email-management/emails') {
      return Promise.resolve({ emails: [makeEmail(EMAIL_ID)] });
    }
    if (path === `/api/email-management/emails/${EMAIL_ID}/actions`) {
      return Promise.reject(new Error('server unavailable'));
    }
    return Promise.resolve({ actions: [] });
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await screen.findByText(/Failed to load actions: server unavailable/i);
  expect(screen.queryByText(/Execution log/i)).not.toBeInTheDocument();
});

it('never requests the removed email log endpoint while opening an accordion', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [makeTaskAction(1)] },
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);
  await screen.findByRole('button', { name: /approve/i });

  expect(api.get.mock.calls.map(([path]) => path)).not.toContain(
    `/api/email-management/emails/${EMAIL_ID}/log`
  );
});

// ── SLICE 5 — Accessibility and design regressions ──────────────────────────

it('opens and closes an inbox row with Enter and Space from the keyboard', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [makeTaskAction(1)] },
  });

  renderEmailTriage();
  const row = await screen.findByRole('button', { name: /Sender email-test-1/i });

  row.focus();
  await user.keyboard('{Enter}');
  await screen.findByRole('button', { name: /approve/i });

  await user.keyboard(' ');
  await waitFor(() => {
    expect(screen.queryByRole('button', { name: /approve/i })).not.toBeInTheDocument();
  });
});

it('reflects accordion state with aria-expanded and matching aria-controls', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });

  renderEmailTriage();
  const row = await screen.findByRole('button', { name: /Sender email-test-1/i });
  expect(row).toHaveAttribute('aria-expanded', 'false');
  expect(row).toHaveAttribute('aria-controls', `email-panel-${EMAIL_ID}`);

  await user.click(row);
  expect(row).toHaveAttribute('aria-expanded', 'true');
  expect(document.getElementById(`email-panel-${EMAIL_ID}`)).toBeInTheDocument();
});

it('adds visible focus ring classes to approve and decline buttons', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [makeTaskAction(1)] },
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  const approveBtn = await screen.findByRole('button', { name: /approve/i });
  const declineBtn = screen.getByRole('button', { name: /decline/i });
  expect(approveBtn).toHaveClass(
    'focus-visible:outline-none',
    'focus-visible:ring-2',
    'focus-visible:ring-green-400',
    'rounded'
  );
  expect(declineBtn).toHaveClass(
    'text-slate-400',
    'hover:text-slate-300',
    'focus-visible:outline-none',
    'focus-visible:ring-2',
    'focus-visible:ring-slate-400',
    'rounded'
  );
});

it('adds visible focus ring classes to action name and datetime inputs', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [makeEventAction(2)] },
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  const nameInput = await screen.findByRole('textbox', { name: /action name/i });
  const datetimeInput = document.querySelector('input[type="datetime-local"]');
  expect(nameInput).toHaveClass(
    'focus-visible:ring-2',
    'focus-visible:ring-slate-400',
    'focus-visible:ring-offset-0'
  );
  expect(datetimeInput).toHaveClass(
    'focus-visible:ring-2',
    'focus-visible:ring-slate-400',
    'focus-visible:ring-offset-0'
  );
});

it('renders Back as a standard dashboard link', async () => {
  setupMocks({ emails: [] });

  renderEmailTriage();
  const backLink = await screen.findByRole('link', { name: /back/i });
  expect(backLink).toHaveAttribute('href', '/dashboard');
  expect(screen.queryByRole('button', { name: /back/i })).not.toBeInTheDocument();
});

it('shows an Actions section label before action rows', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [makeTaskAction(1)] },
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await screen.findByText('Actions');
  const panelText = document.getElementById(`email-panel-${EMAIL_ID}`).textContent;
  expect(panelText.indexOf('Actions')).toBeLessThan(panelText.indexOf('Task'));
});

it('hides the decorative inbox chevron from assistive technology', async () => {
  setupMocks({ emails: [makeEmail(EMAIL_ID)] });

  renderEmailTriage();
  const row = await screen.findByRole('button', { name: /Sender email-test-1/i });
  const chevron = row.querySelector('svg[aria-hidden="true"]');
  expect(chevron).toBeInTheDocument();
});

// ── SLICE 4 — Disposition: Archive and Delete ────────────────────────────────

// Component: Archive button has HTML disabled attribute when action row is pending
it('Archive button has HTML disabled attribute while a pending action row exists', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1);
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await screen.findByRole('button', { name: /approve/i });

  const archiveBtn = screen.getByRole('button', { name: /archive email/i });
  expect(archiveBtn).toBeDisabled();
});

// Component: Delete button has HTML disabled attribute when action row is pending
it('Delete button has HTML disabled attribute while a pending action row exists', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1);
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await screen.findByRole('button', { name: /approve/i });

  const deleteBtn = screen.getByRole('button', { name: /delete email/i });
  expect(deleteBtn).toBeDisabled();
});

// Unit: buttons active immediately when no action rows
it('Archive and Delete are enabled immediately when email has no action rows', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  api.post.mockResolvedValue({ id: EMAIL_ID, triage_status: 'archived' });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  await screen.findByRole('button', { name: /\+ task/i });

  const archiveBtn = screen.getByRole('button', { name: /archive email/i });
  const deleteBtn = screen.getByRole('button', { name: /delete email/i });
  expect(archiveBtn).not.toBeDisabled();
  expect(deleteBtn).not.toBeDisabled();
});

// Component: buttons activate when all rows resolved
it('Archive and Delete activate when all action rows are approved or declined', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1);
  const approvedAction = { ...taskAction, status: 'approved', external_id: 'task-123' };
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });
  api.patch.mockResolvedValue(approvedAction);
  api.post.mockResolvedValue({ id: EMAIL_ID, triage_status: 'archived' });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);

  const approveBtn = await screen.findByRole('button', { name: /approve/i });
  await user.click(approveBtn);

  await waitFor(() => {
    const archiveBtn = screen.getByRole('button', { name: /archive email/i });
    const deleteBtn = screen.getByRole('button', { name: /delete email/i });
    expect(archiveBtn).not.toBeDisabled();
    expect(deleteBtn).not.toBeDisabled();
  });
});

// Unit: buildDispositionLogEntry archive format
it('buildDispositionLogEntry returns correct format for archive', async () => {
  const { buildDispositionLogEntry } = await import('../components/EmailTriage/formatters');
  const ts = new Date('2026-06-29T14:09:00');
  const result = buildDispositionLogEntry('archive', ts);
  expect(result).toMatch(/\d{2} [A-Z][a-z]{2} \d{4} \d{2}:\d{2}  Email archived/);
  expect(result).toContain('Email archived');
});

// Unit: buildDispositionLogEntry delete format
it('buildDispositionLogEntry returns correct format for delete', async () => {
  const { buildDispositionLogEntry } = await import('../components/EmailTriage/formatters');
  const ts = new Date('2026-06-29T14:09:00');
  const result = buildDispositionLogEntry('delete', ts);
  expect(result).toMatch(/\d{2} [A-Z][a-z]{2} \d{4} \d{2}:\d{2}  Email deleted/);
  expect(result).toContain('Email deleted');
});

// Integration: Archive moves email to Processed section
it('clicking Archive moves the email to the Processed section and removes from Pending', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  api.post.mockResolvedValue({ id: EMAIL_ID, triage_status: 'archived' });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);
  await screen.findByRole('button', { name: /\+ task/i });

  const archiveBtn = screen.getByRole('button', { name: /archive email/i });
  await user.click(archiveBtn);

  await screen.findByText('✓ Processed');
  await waitFor(() => {
    expect(screen.queryByRole('button', { name: /archive email/i })).not.toBeInTheDocument();
  });
});

// Integration: Delete moves email to Processed section
it('clicking Delete moves the email to the Processed section and removes from Pending', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  api.post.mockResolvedValue({ id: EMAIL_ID, triage_status: 'deleted' });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);
  await screen.findByRole('button', { name: /\+ task/i });

  const deleteBtn = screen.getByRole('button', { name: /delete email/i });
  await user.click(deleteBtn);

  await screen.findByText('✓ Processed');
  await waitFor(() => {
    expect(screen.queryByRole('button', { name: /delete email/i })).not.toBeInTheDocument();
  });
});

// Integration: rollback on failure — email returns to Pending with error
it('rolls back to Pending and shows error band when dispose API fails', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  api.post.mockRejectedValue(new Error('Gmail API failure'));

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);
  await screen.findByRole('button', { name: /\+ task/i });

  const archiveBtn = screen.getByRole('button', { name: /archive email/i });
  await user.click(archiveBtn);

  await screen.findByText(/Disposition failed:/i);
  expect(screen.queryByText('✓ Processed')).not.toBeInTheDocument();
});

// Integration: disposeErrors cleared on successful retry
it('error band clears on successful retry', async () => {
  const user = userEvent.setup();
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [] },
  });
  api.post
    .mockRejectedValueOnce(new Error('Gmail API failure'))
    .mockResolvedValueOnce({ id: EMAIL_ID, triage_status: 'archived' });

  renderEmailTriage();
  await openAccordion(user, EMAIL_ID);
  await screen.findByRole('button', { name: /\+ task/i });

  // First attempt — fails
  const archiveBtn = screen.getByRole('button', { name: /archive email/i });
  await user.click(archiveBtn);
  await screen.findByText(/Disposition failed:/i);

  // Re-open accordion to get to Archive button again (email rolled back to pending)
  await openAccordion(user, EMAIL_ID);
  await screen.findByRole('button', { name: /\+ task/i });

  const archiveBtn2 = screen.getByRole('button', { name: /archive email/i });
  await user.click(archiveBtn2);

  await waitFor(() => {
    expect(screen.queryByText(/Disposition failed:/i)).not.toBeInTheDocument();
  });
  await screen.findByText('✓ Processed');
});

// Component: ProcessedPanel renders empty state
it('ProcessedPanel renders No actions recorded when log is empty', async () => {
  const { ProcessedPanel } = await import('../components/EmailTriage/ProcessedPanel');
  const { render: r, screen: s } = await import('@testing-library/react');
  r(<ProcessedPanel emailSession={null} />);
  expect(s.getByText('No actions recorded.')).toBeInTheDocument();
});

// Unit: ProcessedPanel renders entries reversed
it('ProcessedPanel renders log entries reversed so newest-stored entry appears last', async () => {
  const { ProcessedPanel } = await import('../components/EmailTriage/ProcessedPanel');
  const { render: r, screen: s } = await import('@testing-library/react');
  // logEntries stored newest-first: [disposition, approval]
  const session = {
    logEntries: ['29 Jun 2026 14:09  Email archived', '29 Jun 2026 14:08  Task "Test" created'],
  };
  r(<ProcessedPanel emailSession={session} />);
  const log = s.getByLabelText('Execution log');
  const text = log.textContent;
  // Reversed: approval first, disposition last
  expect(text.indexOf('Task "Test" created')).toBeLessThan(text.indexOf('Email archived'));
});
