# SOP-003 — Editorial image genereren via ChatGPT DALL-E

**Domein:** Kamer E-commerce — Tricolarae
**Eigenaar:** Nova (workflow) / Owner (uitvoering)
**Trigger:** Nieuwe Look aanmaken voor een Edit (Spring, Summer, Fall, Winter)

---

## Doel

Een consistente editorial fashion image genereren die als hero dient voor een Look op de Tricolarae store. De image toont het gevoel van het outfit (top + layer + pants) zonder een exacte productreproductie te zijn.

---

## Stap-voor-stap

### Stap 1 — Productafbeeldingen verzamelen
Haal de productafbeeldingen op van de 3 Trendsi-producten voor de Look:
- `top.jpg` — de top
- `layer.jpg` — de layer (kimono, cardigan, blazer)
- `pants.jpg` — de broek

### Stap 2 — ChatGPT openen (Plus abonnement vereist)
- Open een **nieuwe chat** in ChatGPT (niet "Create Image" knop — gewone chat)
- Upload alle 3 productafbeeldingen in hetzelfde bericht

### Stap 3 — Prompt sturen
Stuur de afbeeldingen samen met dit prompt-template in **één bericht**:

```
Here are 3 product images (top, layer/cardigan, pants). Use them as color and 
style reference and generate an editorial fashion photograph: a female model 
wearing a [KLEUR + STIJL top], a [KLEUR + STIJL layer] draped loosely over 
her shoulders, and [KLEUR + STIJL pants]. Full body shot, model relaxed, 
layer falling open naturally.

Setting: minimal indoor studio, soft natural side window light, clean 
off-white background.
Mood: effortless, understated, elevated everyday style.
Shot style: fashion editorial, analog film aesthetic, warm earth tone palette.
Portrait orientation.
```

Vervang de `[KLEUR + STIJL]` velden op basis van de werkelijke producten.

### Stap 4 — Consistentie Look II en III
Blijf in **dezelfde ChatGPT chat**. Upload de volgende 3 productafbeeldingen en gebruik:

```
Using the exact same model, studio setting, and lighting from the image above, 
now show her wearing these 3 new pieces instead: [beschrijving Look 2]. 
Same pose style, same background, only the outfit changes.
```

### Stap 5 — Opslaan en uploaden
- Download de gegenereerde image
- Sla op als `look-[nummer]-editorial.png`
- Sasha uploadt naar Shopify via `themeFileUpsert` en koppelt aan de Look-sectie

---

## Kwaliteitscheck

- [ ] Kleurpalet klopt met de 3 producten
- [ ] Silhouetten herkenbaar (wide leg, open cardigan, etc.)
- [ ] Sfeer is editorial (niet generiek stock foto)
- [ ] Achtergrond is clean en consistent met andere Looks

---

## Notities

- DALL-E reproduceert geen exacte kledingstukken -- het vangt stijl en kleur
- Dit is geen blokkade: editorial images verkopen het gevoel, niet het product
- Model-consistentie over Looks: werkt het best binnen dezelfde ChatGPT chat
- Bij grote afwijking: voeg fysieke beschrijving van model toe aan prompt

---

*Aangemaakt: 2026-05-19*
*Gevalideerd: ja — eerste test met top/layer/pants producten geslaagd*
