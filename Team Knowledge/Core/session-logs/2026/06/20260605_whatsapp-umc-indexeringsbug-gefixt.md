# WhatsApp UMC indexeringsbug gefixt — 2026-06-05

**Session date:** 2026-06-05
**Topics:** whatsapp, umc, bugfix, infra

## Summary

Bug geidentificeerd in whatsapp_export_handler.py: dubbel Team Knowledge in padberekening naar memory-db waardoor UMC-indexering bij elke export werd overgeslagen. Kai heeft regel 29 gecorrigeerd van parents[3] / Team Knowledge / ... naar parents[1] / memory-db. Fix geverifieerd — pad resolveert nu correct naar /opt/myPKA/Team Knowledge/Core/Integrations/memory-db.
