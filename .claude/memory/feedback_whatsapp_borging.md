---
name: feedback-whatsapp-borging
description: When saving WhatsApp conversations always store the full text including quoted messages
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4b3957ab-21c0-4acd-9770-55a5b389fa48
---

When saving WhatsApp conversations in P-Scheiding (or elsewhere): always store the full text, including the text being replied to.

WhatsApp replies contain a quoted message above the actual message. Omitting that quote can cause context to be lost — conversations then become hard to follow.

**Why:** Walter has explicitly stated this is important, because WhatsApp threads in a separation context serve as evidence and reference material.

**How to apply:** For every WhatsApp chat log being saved: the duplication is not an error but a reply-quote. Preserve both. Clearly note who the sender is and which message is being replied to. All message texts always in quotes — both the message content itself and the quoted text in a reply. Format: *(reply to: "quoted text")* and the message content as `"text"`.
