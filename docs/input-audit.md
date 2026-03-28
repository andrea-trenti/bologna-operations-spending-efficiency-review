# Input Audit

This document records the exact Bologna files used in the project.

## Files used in the analysis

| File name | Type | Used in project | Main analytical role |
|---|---|---:|---|
| `Bilancio di Previsione 2025_2027.pdf` | PDF | Yes | legal 2025–2027 budget envelope |
| `Piano esecutivo di gestione assestato 2025_2027.pdf` | PDF | Yes | PEG chapters, earmarks, and optimisation floors |
| `Rendiconto 2024.pdf` | PDF | Yes | realised commitments, payments, FPV, and result of administration |
| `bilancio-di-previsione-previsione-uscite.csv` | CSV | Yes | computable budget cross-checks |
| `rendiconto-di-gestione-rendiconto-uscite.csv` | CSV | Yes | computable execution ratios |
| `gare-e-appalti.csv` | CSV | Yes | procurement structure and throughput |
| `lavori-pubblici-storico.csv` | CSV | Yes | historical works profile |
| `lavori-pubblici.csv` | CSV | Yes | current workstock and disruption load |
| `segnalazioni-open-citizen-relationship-management-czrm.csv` | CSV | Yes | demand, complaint pressure, and backlog proxy |
| `traffico-viali.csv` | CSV | Yes | corridor traffic criticality |
| `tpl_validazioni_km.csv` | CSV | Yes | modal exposure and validations-per-km |
| `incidenti_new.csv` | CSV | Yes | safety risk and hotspot weighting |

## Files not included in this repository

- raw CSV files;
- raw PDF files;
- locally extracted text files derived from PDFs.

The repository contains the writing, code, and source documentation. The original files can be downloaded from the official pages listed in `docs/data-sources.md`.

## Final note

The project uses only the Bologna-focused material listed above. No unrelated material is part of this repository.
