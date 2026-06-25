# SOP: Build a Full-Stack Feature

> **Default owner:** Devon. Any agent can invoke this skill when implementing a narrow end-to-end feature slice.

Devon's signature workflow for building a production-ready full-stack feature across frontend, backend, typed contracts, tests and handoff, without crossing specialist boundaries.

## When this skill activates

Invoke this SOP when Larry routes work such as:

- "Build this feature end-to-end."
- "Add this screen and make it work with the backend."
- "Create the endpoint and wire the UI to it."
- "Implement this dashboard backed by existing data."
- "Frontend and backend are out of sync."
- "Make this feature production-ready."
- "Add tests around this full-stack behavior."
- "Refactor this feature without changing behavior."

If the work is purely WordPress-specific, route to Finn.

If the work is purely Shopify-specific, route to Sasha.

If the work requires infrastructure architecture, deployment architecture or integration architecture, route to Kai before Devon builds.

If the work requires project sequencing or delivery control, route to Marcus.

If the work needs final quality verification, route to Vera after Devon completes the build.

## Procedure

### 1. Confirm the feature slice

Before writing code, identify the smallest useful feature slice.

Clarify or document:

- User-facing behavior.
- Backend behavior.
- Data inputs.
- Data outputs.
- Loading state.
- Empty state.
- Error state.
- Success state.
- Permission or auth assumptions.
- Existing data source.
- Tests expected.
- Out-of-scope items.

If the feature cannot be described as a narrow slice, ask Larry to reduce scope before building.

### 2. Inspect the codebase

Read before editing.

Inspect:

- Existing frontend structure.
- Existing backend structure.
- Existing API routes or handlers.
- Existing service, domain and repository patterns.
- Existing state or query layer.
- Existing test patterns.
- Existing type definitions.
- Existing design-system usage.
- Existing error handling patterns.

Do not introduce a new pattern unless Larry explicitly authorizes it.

### 3. Identify specialist boundaries

Before implementation, check whether the feature requires:

- New architecture.
- New infrastructure.
- New deployment path.
- External integration architecture.
- WordPress-specific implementation.
- Shopify-specific implementation.
- Ads implementation.
- Product sourcing or operations workflow.
- Security-sensitive auth or permission logic.
- Final QA or accessibility sign-off.

Route as follows:

| Boundary | Owner |
|---|---|
| Orchestration and Owner-facing control | Larry |
| Infrastructure, deployment and integration architecture | Kai |
| Project sequencing and delivery control | Marcus |
| WordPress implementation | Finn |
| Shopify implementation | Sasha |
| Governance control | Iris |
| Market validation | Bo |
| Final QA, responsive and regression gate | Vera |
| Ads and acquisition implementation | Zara |
| E-commerce operations | Nova |
| Product intelligence | Remy |

Devon may continue only when the boundary is already approved, already exists or is explicitly out of scope.

### 4. Define the typed contract

Before connecting layers, define the contract.

Depending on the project, this may include:

- Request body type.
- Response type.
- Error response type.
- Domain input type.
- Domain output type.
- Frontend view model type.
- API client function type.
- Store or query result type.

Rules:

- No `any`.
- No implicit `any`.
- No unexplained type suppression.
- Do not let untyped network data flow directly into UI rendering.
- Keep contracts close to existing project conventions.

### 5. Implement the backend path

Implement only the backend behavior required for the feature slice.

Typical order:

1. Add or update pure domain logic.
2. Add or update service function.
3. Add or update repository usage if the persistence path already exists.
4. Add or update API route or handler.
5. Add input validation at the correct boundary.
6. Add typed success response.
7. Add typed error behavior.
8. Add tests.

Do not create broad architecture, deployment or integration changes unless Kai has routed and approved that work.

### 6. Implement the frontend path

Implement the frontend integration using existing patterns.

Typical order:

1. Add or update typed API client.
2. Add or update query, mutation or store usage.
3. Add or update page, component or view.
4. Handle loading, empty, error, success and disabled states when relevant.
5. Use existing design-system tokens and primitives.
6. Preserve accessibility: semantic HTML, keyboard navigation, visible focus indicators and correct ARIA where needed.
7. Add tests when the project supports frontend tests.

### 7. Add or update tests

Testing is part of the build.

Choose the smallest useful test set first.

Possible tests:

- Unit tests for pure logic.
- Service tests for backend behavior.
- API route tests for request and response behavior.
- Frontend component tests.
- Integration tests for frontend/backend contract behavior.
- Regression tests for bugs.

Every fixed bug needs a regression test unless Larry explicitly scopes it out.

### 8. Run validation

Run validation in this order when feasible:

1. Format or lint check used by the project.
2. Type check.
3. Focused tests for changed area.
4. Broader relevant test suite.
5. Full test suite if feasible.
6. Manual local check for user-facing behavior when the feature has UI.

If a validation step is skipped, record why in the final report and session-log.

### 9. Self-review before handoff

Before reporting done, inspect the diff.

Check:

- Scope stayed narrow.
- No unrelated files changed.
- No new top-level folders introduced without approval.
- No hardcoded design values if tokens exist.
- No untyped contracts.
- No specialist boundaries crossed.
- Error states exist.
- Tests match behavior.
- Naming matches project conventions.
- No secrets or credentials added.
- No hidden background processes introduced.
- No accidental production behavior introduced.

### 10. Write session-log entry

Write a session-log entry at:

`Team Knowledge/Core/session-logs/YYYY/MM/YYYY-MM-DD-HH-MM_devon_<feature-slug>.md`

Required frontmatter:

```yaml
---
agent_id: devon
session_id: <session-or-thread-id>
timestamp: <YYYY-MM-DDTHH:MM:SSZ>
type: end-of-session | mid-session-insight | realignment
linked_sops: ["SOP-devon-build-a-full-stack-feature"]
linked_workstreams: []
linked_guidelines: []
---
```

Include:

- Feature summary.
- Files changed.
- Backend behavior added or changed.
- Frontend behavior added or changed.
- Typed contracts added or changed.
- Tests added or run.
- Validation commands and results.
- Specialist handoffs or boundaries.
- Deferred follow-ups.
- Known limitations.

### 11. Hand off to Vera

If the work has user-facing behavior, Larry routes the result to Vera for quality gate.

Vera checks:

- Visual behavior.
- Responsive behavior.
- Accessibility.
- Regression risk.
- Acceptance criteria.
- Final quality sign-off.

Devon fixes issues Vera flags, then resubmits.

## Output / definition of done

A full-stack feature build is done when all of these are true:

- [ ] Scope is narrow and confirmed.
- [ ] Existing frontend and backend patterns were inspected.
- [ ] Specialist boundaries were checked.
- [ ] Architecture, deployment or integration boundaries were not crossed without Kai.
- [ ] Request, response and view contracts are typed.
- [ ] Backend success and error paths are implemented.
- [ ] Frontend loading, empty, error, success and disabled states are handled when relevant.
- [ ] Accessibility basics are preserved.
- [ ] Relevant tests were added or updated.
- [ ] Focused validation was run.
- [ ] Broader validation was run when feasible.
- [ ] Session-log entry was written.
- [ ] Vera handoff happened when user-facing behavior changed.

If any required item is unchecked, the feature is still in progress.
