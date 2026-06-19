# Geldstroom Scan — Testcase

Datum: 2026-05-11
Gebaseerd op: bankexport ING NL17INGB0799281751 — periode 1 feb t/m 10 mei 2026
Uitvoerder: Vera (Geldstroom Regie — methodiek testcase)

---

## 1. Huishoudensprofiel

- Samenstelling: alleenstaande in transitie (scheiding lopend, gezamenlijke rekening met ex-partner nog actief)
- Inkomstentype: loondienst (stabiel)
- Rekeningstructuur: ING betaalrekening (inkomst), gezamenlijke rekening met ex-partner, bunq betaalrekening (privé vaste lasten), ING spaarrekening

---

## 2. Geldstroom 1 — Inkomen

| Inkomstenstroom | Netto bedrag | Frequentie | Rekening |
|---|---|---|---|
| PostNL salaris | €3,600.78 | Maandelijks | ING betaalrekening |
| Zilveren Kruis vergoedingen | Variabel | Onregelmatig | ING betaalrekening |
| Overige (PMI, terugbetalingen, verrekeningen) | Variabel | Onregelmatig | ING betaalrekening |

**Totaal netto inkomen/maand: €3,600.78** *(structureel — variabele stromen buiten beschouwing)*

Inkomen stabiel: ja. Februari afwijkend: €3,748.96 — reden niet opgegeven.

**Regiepunten:**
- ✅ Hoofdinkomen (PostNL) duidelijk gedocumenteerd en stabiel
- ⚠️ Meerdere kleinere inkomstenstromen zichtbaar in export maar niet gedocumenteerd
- ⚠️ Februari-salaris wijkt af — variabiliteit aanwezig, reden onbekend

---

## 3. Geldstroom 2 — Bestedingen

### Vaste lasten zichtbaar in export

| Last | Bedrag | Frequentie | Rekening |
|---|---|---|---|
| Gezamenlijke rekening — vaste lasten (hypotheek, energie, abonnementen, belastingen naar rato) | €773.00 | Maandelijks | Gezamenlijke rekening |
| Gezamenlijke rekening — boodschappen | €476.00 | Maandelijks | Gezamenlijke rekening |
| Zilveren Kruis zorgverzekering | €210.13 | Maandelijks | ING betaalrekening |
| ALLSAFE opslagruimte | €101.00 | Maandelijks | ING betaalrekening |

**Totaal zichtbare vaste lasten/maand: €1,560.13**

### Niet-zichtbare vaste lasten
Verzekeringen, mobiel en abonnementen lopen via bunq betaalrekening. Geen export aangeleverd — bedragen niet inzichtelijk.

### Variabele uitgaven
Zichtbaar in export maar niet gecategoriseerd in deze scan. Bevat o.a. brandstof, kleding, horeca, winkels.

**Verhouding vaste lasten / inkomen: minimaal 43%** *(onvolledig — bunq ontbreekt)*

**Regiepunten:**
- ✅ Grootste vaste lasten (gezamenlijke rekening, zorgverzekering) zichtbaar
- ⚠️ Bestedingen via bunq niet inzichtelijk — deel van de vaste lasten ontbreekt in het overzicht
- ⚠️ Variabele uitgaven zijn niet gestructureerd zichtbaar per categorie
- ❌ Volledig bestedingsoverzicht niet beschikbaar zonder bunq data

---

## 4. Geldstroom 3 — Bescherming

- Buffer: aanwezig op ING spaarrekening — omvang niet in scope van de scan
- Vangnetten: zorgverzekering aanwezig (Zilveren Kruis), overige verzekeringen via bunq aanwezig maar niet gespecificeerd
- Schulden en aflossingen: niet opgegeven — niet inzichtelijk uit de aangeleverde data

**Regiepunten:**
- ✅ Buffer aanwezig
- ⚠️ Verzekeringsdekking aanwezig maar niet volledig gedocumenteerd in deze scan
- ❌ Schulden en betalingsregelingen niet in kaart gebracht

---

## 5. Geldstroom 4 — Groei

- Spaarcapaciteit: niet berekend — bestedingen onvolledig (bunq ontbreekt)
- Spaarstructuur: ING spaarrekening aanwezig, saldo onbekend
- Spaarbijdrage: onregelmatig — alleen als er iets overblijft, geen vaste maandelijkse overboeking
- Pensioen/beleggingen: niet opgegeven

**Regiepunten:**
- ⚠️ Spaarrekening aanwezig maar zonder structurele maandelijkse bijdrage
- ❌ Geen geborgde spaarcapaciteit zichtbaar in het geldsysteem
- ❌ Vrije ruimte niet kwantificeerbaar door incomplete bestedingsdata

---

## 6. Regiesignalen

1. We zien dat bestedingen via de bunq betaalrekening niet zichtbaar zijn in het aangeleverde overzicht. Dit verdient aandacht.
2. We zien dat sparen onregelmatig plaatsvindt — alleen als er iets overblijft, zonder vaste structuur. Dit verdient aandacht.
3. We zien dat de financiële structuur in transitie is (gezamenlijke rekening met ex-partner nog actief). Dit verdient aandacht.
4. We zien dat kleinere inkomstenstromen zichtbaar zijn in de export maar niet gedocumenteerd zijn. Dit verdient aandacht.
5. We zien dat schulden en betalingsregelingen niet in kaart zijn gebracht. Dit verdient aandacht.

---

## 7. Doorverwijzingen

- Voor de afwikkeling van de gezamenlijke financiële structuur (scheiding) verwijzen wij naar een erkend specialist. Dit valt buiten de functionele structuur van Geldstroom Regie.

---

## 8. Disclaimer

Dit Scan is een functioneel inzichtsdocument. Het bevat geen financieel, fiscaal, juridisch, verzekerings-, hypotheek- of beleggingsadvies. Voor specialistisch advies verwijzen wij naar een erkend specialist.

---

## Methodiekaantekeningen (intern — niet voor klant)

Gevonden gaps in SOP-002 tijdens deze testcase:

1. **Gezamenlijke rekeningen worden niet spontaan gemeld.** De intakevraag over rekeningstructuur moet expliciet vragen naar gezamenlijke rekeningen.
2. **Bunq-probleem:** het besluit "alleen inkomstrekening export nodig" werkt niet als vaste lasten via een tweede rekening lopen. Aanvulling nodig: als vaste lasten zichtbaar via een tweede rekening lopen, is een export van die rekening wel nodig voor een volledig bestedingsoverzicht.
3. **Transitiesituatie (scheiding) ontbreekt als scenario in SOP-002.** Dit vraagt een eigen aanpak — de structuur is tijdelijk en de scan legt dat bloot.
4. **Spaarcapaciteit berekenen lukt niet zonder volledig bestedingsoverzicht.** SOP-002 gaat ervan uit dat alle bestedingen zichtbaar zijn — dat is in de praktijk niet altijd het geval.

---

Delivered on: 2026-05-11
Delivered at: Deliverables/20260511_Geldstroom Regie_Scan testcase/
