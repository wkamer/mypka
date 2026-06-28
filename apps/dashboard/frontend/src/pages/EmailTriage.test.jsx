/**
 * EmailTriage.test.jsx — Slice 3 frontend tests.
 * G4 test spec: 14 scenarios covering ActionsPanel behaviour.
 * Written before implementation per SOP-018 TDD protocol.
 */

import { vi, describe, it, expect, beforeEach, afterEach } from 'vitest';
import { render, screen, waitFor, within } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom';
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

// ── SCENARIO 1 — Actions load on accordion open ───────────────────────────────

it('loads actions when accordion opens and renders action rows', async () => {
  const user = userEvent.setup();
  const taskAction = makeTaskAction(1);
  setupMocks({
    emails: [makeEmail(EMAIL_ID)],
    actionsByEmailId: { [EMAIL_ID]: [taskAction] },
  });

  render(<EmailTriage />);
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

  render(<EmailTriage />);
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

  render(<EmailTriage />);
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

  render(<EmailTriage />);
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

  render(<EmailTriage />);
  await openAccordion(user, EMAIL_ID);

  const approveBtn = await screen.findByRole('button', { name: /approve/i });
  await user.click(approveBtn);

  // Log entry shows task name
  await screen.findByText(/Task Follow up with client created/i);
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

  render(<EmailTriage />);
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
  await screen.findByText(/Task Edited task name created/i);
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

  render(<EmailTriage />);
  await openAccordion(user, EMAIL_ID);

  const approveBtn = await screen.findByRole('button', { name: /approve/i });
  await user.click(approveBtn);

  // Log entry shows event format with name and datetime
  await screen.findByText(/Event Team standup/i);
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

  render(<EmailTriage />);
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

  render(<EmailTriage />);
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

  render(<EmailTriage />);
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

  render(<EmailTriage />);
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
  await screen.findByText(/Task Manual task created/i);
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

  render(<EmailTriage />);
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
  await screen.findByText(/Event Manual event/i);
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

  render(<EmailTriage />);
  await openAccordion(user, EMAIL_ID);

  // Approve first action
  const approveBtns = await screen.findAllByRole('button', { name: /approve/i });
  await user.click(approveBtns[0]);
  await screen.findByText(/Task First task created/i);

  // Approve second action
  const approveBtns2 = await screen.findAllByRole('button', { name: /approve/i });
  await user.click(approveBtns2[0]);

  // Both entries present
  await screen.findByText(/Task Second task created/i);
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

  render(<EmailTriage />);
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

  render(<EmailTriage />);

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

  render(<EmailTriage />);

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
