---
status: besloten
datum: 2026-05-11
---

# I-Rekeningexports en saldo in de scan

## Methodiekbesluit

Voor de Geldstroom Scan is alleen de export van de **inkomstrekening** noodzakelijk. Exports van spaar- en betaalrekeningen zijn niet verplicht.

## Onderbouwing

**Flows zijn afleidbaar uit de inkomstrekening.**
Alle uitgaande transfers naar andere rekeningen (spaar, bunq, etc.) zijn zichtbaar als transacties in de inkomstrekening. De structuur van het geldsysteem — wat waarheen stroomt — is daarmee volledig reconstrueerbaar zonder extra exports.

**Saldo valt buiten de scan.**
Een saldo is een momentopname van vermogen. De scan vraagt alleen: *is er een buffer aanwezig?* — ja of nee, globaal voldoende of niet. Het exacte bedrag is financieel adviesgebied en hoort niet in de scan.

## Implicaties voor SOP-002

- Intakevraag rekeningstructuur: vraag welke rekeningen er zijn, maar vraag geen exports op van alle rekeningen
- Buffercheck (Bescherming): stel een gerichte ja/nee-vraag — geen saldo opvragen
- Flows naar andere rekeningen: afleiden uit de inkomstrekening export

## Open vraag

- Geldt dit ook voor stellen met gescheiden inkomens op verschillende rekeningen?
