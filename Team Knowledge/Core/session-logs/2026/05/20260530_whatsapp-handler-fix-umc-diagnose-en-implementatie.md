# WhatsApp handler fix + UMC diagnose en implementatie — 2026-05-30

**Session date:** 2026-05-30
**Topics:** umc,whatsapp,infrastructure,agents

## Summary

WhatsApp sync handler schreef nieuwe bestanden naar verkeerde map (PKM/CRM i.p.v. P-Scheiding/WhatsApp); 4 bestanden verplaatst en sync_handler.sh gefixed met slug mapping. Kai diagnosticeerde UMC-gebruik en vond nul specialist-writes, domain naming inconsistentie en niet-werkende sessiestart reads. Drie fixes geïmplementeerd: domain mapping in close_routine_verification.py, SessionStart hook toegevoegd, en alle 14 AGENT.md bestanden bijgewerkt met werkende CLI-instructie.
