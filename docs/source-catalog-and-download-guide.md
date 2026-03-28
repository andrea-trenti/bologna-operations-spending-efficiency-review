# Source Catalog and Download Guide

This document lists the **official source pages** used by the repository, explains what each source contains, why it matters analytically, and how it should be downloaded for local reproducibility.

This public GitHub package does **not** bundle raw municipal files. Instead, it documents the official source pages and expected filenames.

## How to use this guide

1. Open the official page.
2. Download the file in CSV or PDF format.
3. Save it in `data/raw/`.
4. Keep the filename exactly as shown below.

---

## A. Core official municipal documents (PDF)

### 1. Bilancio di Previsione 2025–2027
- **Official page:** `https://www.comune.bologna.it/amministrazione-trasparente/bilanci/bilancio-preventivo-consuntivo/bilancio-preventivo/bilancio-preventivo-comune-bologna-anno-2025`
- **Type:** official budget document (PDF attachments on the page)
- **Save locally as:** `Bilancio di Previsione 2025_2027.pdf`
- **Used for:**
  - legal budget envelopes;
  - Mission 10 / Programme 1002 / Programme 1005 headline appropriations;
  - current vs capital balance framing;
  - fiscal admissibility in Parts 1, 3, 4, and 5.
- **What is analysed from it:** headline expenditure totals, programme allocations, legal ceilings, budget equilibrium logic.

### 2. PEG assestato 2025–2027
- **Official page:** `https://www.comune.bologna.it/amministrazione-trasparente/bilanci/bilancio-preventivo-consuntivo/bilancio-peg-assestato/bilancio-peg-assestato-2025-2027`
- **Type:** official PEG document (PDF attachments on the page)
- **Save locally as:** `Piano esecutivo di gestione assestato 2025_2027.pdf`
- **Used for:**
  - chapter-level appropriations;
  - maintenance and signage floors;
  - earmarks and project-linked lines;
  - optimization constraints in Part 5.
- **What is analysed from it:** chapter families such as `U33500-000`, `U33460-000`, protected project lines, residual/cash logic.

### 3. Rendiconto 2024
- **Official page:** `https://www.comune.bologna.it/amministrazione-trasparente/bilancio-consuntivo-comune-bologna-anno-2024`
- **Type:** official annual-account document (PDF attachments on the page)
- **Save locally as:** `Rendiconto 2024.pdf`
- **Used for:**
  - result of administration;
  - commitment/payment realization;
  - programme-level execution anchors;
  - legal closed-year comparison against the 2025 budget.
- **What is analysed from it:** commitments, competence payments, FPV, available surplus, realised execution in Programmes 1002 and 1005.

---

## B. Bologna Open Data datasets (CSV)

### 4. Budgeted expenditure table
- **Official page:** `https://opendata.comune.bologna.it/explore/dataset/bilancio-di-previsione-previsione-uscite/`
- **Export page:** `https://opendata.comune.bologna.it/explore/dataset/bilancio-di-previsione-previsione-uscite/export/`
- **Save locally as:** `bilancio-di-previsione-previsione-uscite.csv`
- **Used for:** computational budget slicing and programme comparisons in Parts 1–5.
- **What is analysed from it:** mission/programme totals, computable budget perimeter, cross-checks against the legal PDF.

### 5. Annual-account expenditure table
- **Official page:** `https://opendata.comune.bologna.it/explore/dataset/rendiconto-di-gestione-rendiconto-uscite/`
- **Export page:** `https://opendata.comune.bologna.it/explore/dataset/rendiconto-di-gestione-rendiconto-uscite/export/`
- **Save locally as:** `rendiconto-di-gestione-rendiconto-uscite.csv`
- **Used for:** commitment-conversion ratios, payment ratios, FPV intensity, and programme-level execution in Parts 1, 3, 4, and 5.
- **What is analysed from it:** 2024 execution by mission/programme/title, Title-2 activation in Programmes 1002 and 1005.

### 6. Procurement archive
- **Official page:** `https://opendata.comune.bologna.it/explore/dataset/gare-e-appalti/`
- **Export page:** `https://opendata.comune.bologna.it/explore/dataset/gare-e-appalti/export/`
- **Save locally as:** `gare-e-appalti.csv`
- **Used for:** procurement structure, lot fragmentation, award/liquidation pipeline, and mobility-maintenance filtering in Parts 3–5.
- **What is analysed from it:** procedure types, appalto types, awarded value, liquidated value, mobility-related subset, handling-capacity proxies.

### 7. Historical public works
- **Official page:** `https://opendata.comune.bologna.it/explore/dataset/lavori-pubblici-storico/`
- **Export page:** `https://opendata.comune.bologna.it/explore/dataset/lavori-pubblici-storico/export/`
- **Save locally as:** `lavori-pubblici-storico.csv`
- **Used for:** historical work typology, duration priors, territorial coverage, and lagged supply footprint in Parts 2–5.
- **What is analysed from it:** roads vs sidewalks vs bridges mix, completed-work duration profile, quartiere distribution.

### 8. Current public works
- **Official page:** `https://opendata.comune.bologna.it/explore/dataset/lavori-pubblici/`
- **Export page:** `https://opendata.comune.bologna.it/explore/dataset/lavori-pubblici/export/`
- **Save locally as:** `lavori-pubblici.csv`
- **Used for:** current workstock, tram-related concentration, disruption capacity, and territorial under-coverage in Parts 2–5.
- **What is analysed from it:** active works by type, quartiere distribution, elapsed durations, workstock saturation.

### 9. Citizen-ticket archive (CZRM)
- **Official page:** `https://opendata.comune.bologna.it/explore/dataset/segnalazioni-open-citizen-relationship-management-czrm/`
- **Export page:** `https://opendata.comune.bologna.it/explore/dataset/segnalazioni-open-citizen-relationship-management-czrm/export/`
- **Save locally as:** `segnalazioni-open-citizen-relationship-management-czrm.csv`
- **Used for:** core demand and backlog signal in Parts 1–5.
- **What is analysed from it:** total complaints, road-space complaint subset, spatial concentration, monthly seasonality, forecasting target variables.

### 10. Traffic counts on major viali
- **Official page:** `https://opendata.comune.bologna.it/explore/dataset/traffico-viali/`
- **Export page:** `https://opendata.comune.bologna.it/explore/dataset/traffico-viali/export/`
- **Save locally as:** `traffico-viali.csv`
- **Used for:** corridor criticality and mobility exposure in Parts 1, 2, 4, and 5.
- **What is analysed from it:** annual traffic totals, corridor concentration, disruption and network-criticality weights.

### 11. Public-transport validations and kilometres
- **Official page:** `https://opendata.comune.bologna.it/explore/dataset/tpl_validazioni_km/`
- **Export page:** `https://opendata.comune.bologna.it/explore/dataset/tpl_validazioni_km/export/`
- **Save locally as:** `tpl_validazioni_km.csv`
- **Used for:** modal exposure and validations-per-km logic in Parts 1, 2, 4, and 5.
- **What is analysed from it:** urban validations, service kilometres, validations-per-km intensity.

### 12. Incident statistics
- **Official page:** `https://opendata.comune.bologna.it/explore/dataset/incidenti_new/`
- **Export page:** `https://opendata.comune.bologna.it/explore/dataset/incidenti_new/export/`
- **Save locally as:** `incidenti_new.csv`
- **Used for:** safety risk and hotspot weighting in Parts 1, 2, 4, and 5.
- **What is analysed from it:** incidents, injuries, deaths, quartiere concentration, annual evolution.

---

## C. Contextual and institutional sources used in the introduction

### 13. University of Bologna history
- **Official page:** `https://www.unibo.it/en/university/who-we-are/our-history`
- **Used for:** historical framing in `papers/bologna-context-and-motivation.md`.
- **What is analysed from it:** the University’s conventional 1088 foundation date and institutional continuity.

### 14. Birth of the Studium and the Commune
- **Official page:** `https://www.unibo.it/en/university/who-we-are/our-history/nine-centuries-of-history/the-birth-of-the-studium-and-the-commune`
- **Used for:** contextual discussion of Bologna’s historical institutional development.
- **What is analysed from it:** relationship between the medieval city and the university.

### 15. UNESCO: The Porticoes of Bologna
- **Official page:** `https://whc.unesco.org/en/list/1650/`
- **Used for:** contextual discussion of Bologna’s urban form in the introduction paper.
- **What is analysed from it:** UNESCO inscription, 12 component parts, and the broader 62 km portico system.

---

## D. Legal and publication references

### 16. Comune di Bologna legal notes
- **Official page:** `https://www.comune.bologna.it/informazioni/note-legali-v03`
- **Used for:** publication and attribution note in this GitHub package.
- **What is analysed from it:** site content is released under CC BY 4.0 with attribution obligations.

### 17. Bologna Open Data portal
- **Official page:** `https://opendata.comune.bologna.it/explore/`
- **Used for:** source verification and open-data portal documentation.
- **What is analysed from it:** official dataset catalogue and public source environment.

### 18. D.Lgs. 118/2011
- **Reference:** Italian harmonised public-accounting framework for territorial entities.
- **Used for:** Parts 1, 4, and 5.
- **What is analysed from it:** legal structure of local accounting, competence, FPV, and result of administration.

### 19. D.Lgs. 267/2000 (TUEL)
- **Reference:** Italian local-authority legal framework.
- **Used for:** Parts 1 and 5.
- **What is analysed from it:** municipal budget and public-administration legal structure.

### 20. D.Lgs. 36/2023
- **Reference:** Italian public procurement code.
- **Used for:** Parts 3 and 5.
- **What is analysed from it:** public-procurement framework relevant to procedure design and contract handling.

---

## Recommended local folder layout

```text
project-root/
  data/
    raw/
      Bilancio di Previsione 2025_2027.pdf
      Piano esecutivo di gestione assestato 2025_2027.pdf
      Rendiconto 2024.pdf
      bilancio-di-previsione-previsione-uscite.csv
      rendiconto-di-gestione-rendiconto-uscite.csv
      gare-e-appalti.csv
      lavori-pubblici-storico.csv
      lavori-pubblici.csv
      segnalazioni-open-citizen-relationship-management-czrm.csv
      traffico-viali.csv
      tpl_validazioni_km.csv
      incidenti_new.csv
```

## Bottom line

This repository is intentionally designed so that a public GitHub version can remain clean and source-linked, while still allowing any reader to reconstruct the full analytical workflow locally.
