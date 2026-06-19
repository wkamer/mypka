---
name: feedback_gl017_cleanup_cycle_g2
description: "During a cleanup cycle, batch proposals, correction notes, execution plans, and verification reports are G2 artifacts — they go inside the active control folder, not standalone folders."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ae2d81e8-393d-4ab4-bc1e-517742267593
---

Do not create a new Deliverables folder for batch proposals, correction notes, execution plans, or verification reports within a cleanup cycle.

**Why:** These are supporting artifacts within an active workstream, not primary deliverables. The cleanup cycle already has an active control folder that is the correct home.

**How to apply:** When writing a batch proposal, correction, or execution plan during a DL cleanup cycle, write it as a file inside the existing active control folder (e.g., `20260612_Core_DL Control Inventory/`). Only create a new standalone folder if GL-017 G1 criteria are affirmatively met — which for cleanup-cycle supporting documents they are not. Default is G2. Uncertainty resolves to G2.
