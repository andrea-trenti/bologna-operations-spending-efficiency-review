# Input Usage Audit

This file records the exact Bologna inputs used in the repository.

## Bologna files used in the analysis

| File name | Type | Used in project | Main analytical role |
|---|---|---:|---|
| `Bilancio di Previsione 2025_2027.pdf` | PDF | Yes | legal 2025–2027 budget envelope |
| `Piano esecutivo di gestione assestato 2025_2027.pdf` | PDF | Yes | PEG chapters, earmarks, and optimization floors |
| `Rendiconto 2024.pdf` | PDF | Yes | realized commitments, payments, FPV, and result of administration |
| `bilancio-di-previsione-previsione-uscite.csv` | CSV | Yes | computable budget cross-checks |
| `rendiconto-di-gestione-rendiconto-uscite.csv` | CSV | Yes | computable execution ratios |
| `gare-e-appalti.csv` | CSV | Yes | procurement structure and throughput |
| `lavori-pubblici-storico.csv` | CSV | Yes | historical works profile |
| `lavori-pubblici.csv` | CSV | Yes | current workstock and disruption load |
| `segnalazioni-open-citizen-relationship-management-czrm.csv` | CSV | Yes | demand, complaint pressure, and backlog proxy |
| `traffico-viali.csv` | CSV | Yes | corridor traffic criticality |
| `tpl_validazioni_km.csv` | CSV | Yes | modal exposure and validations-per-km |
| `incidenti_new.csv` | CSV | Yes | safety risk and hotspot weighting |

## Files intentionally excluded from this public GitHub package

- raw CSV files;
- raw PDF files;
- locally extracted text files derived from PDFs;
- unrelated legacy M5/Walmart artifacts.

These files were excluded deliberately to keep the repository leaner, cleaner, and more prudent for public publication. Reproducibility is preserved through `docs/source-catalog-and-download-guide.md`.

## Final audit statement

The analytical repository uses only the Bologna-focused material listed above. No unrelated M5/Walmart content is part of this GitHub-ready package.
