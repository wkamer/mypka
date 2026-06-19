---
name: feedback_whatsapp_umc_lookup
description: "Retrieve WhatsApp messages via UMC get_latest_whatsapp(), never via file discovery"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8bd65bc5-c285-46b7-ae1d-e1fd2bb762c5
---

Always use `mm.get_latest_whatsapp(contact_slug, n_days)` for WhatsApp messages. This takes < 0.2s.

**Why:** File discovery (find + ls + Read) took nearly 1.5 minutes. The data is already in the UMC (memory_knowledge, source_type='whatsapp'). search_knowledge() does not work for "latest messages" because it uses BM25/vector, not date-sorted.

**How to apply:**
```python
mm = get_manager()
results = mm.get_latest_whatsapp("wendy-opdam", n_days=1)
for r in results:
    print(r["chunk_text"])
```

Available slugs: `wendy-opdam`. Contact slug is in the filename (whatsapp-<slug>.md).
Never use find, ls, or Read to search for WhatsApp files when you need recent messages.
