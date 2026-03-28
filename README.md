# Bologna Operations and Spending Efficiency Review

An independent, GitHub-first analytical project on the **Comune di Bologna** focused on public finance, urban demand, procurement, forecasting, and optimization for roads, mobility, and urban maintenance.

This repository was built as a **serious personal project** for intellectual interest, portfolio use, and structured public-sector analysis. The goal is not to publish raw data indiscriminately, but to provide a clean, professional repository containing:

- one coherent analytical narrative;
- six GitHub-ready Markdown papers;
- Python scripts corresponding to the main analytical steps;
- a full source catalog with official links and download instructions;
- publication and attribution notes for a public GitHub setup.

The repository is intentionally configured for **public GitHub publication**:
- no municipal raw files are bundled in the repository;
- official source links are documented in detail;
- scripts assume local downloads placed in `data/raw/`;
- documentation explains exactly what was used, why it was used, and how to reproduce the work.

## Repository structure

- `papers/` — six main Markdown papers: introduction + Parts 1–5.
- `scripts/` — Python scripts mirroring the main analytical workflow.
- `docs/` — source catalog, legal/publication notes, repository setup, file audit, and manifest.
- `requirements.txt` — Python dependencies.
- `.gitignore` — excludes local data downloads and cache files.

## Papers

- `papers/bologna-context-and-motivation.md` — civic context, project motivation, and why Bologna is the right analytical case.
- `papers/municipal-fiscal-architecture-cash-conversion.md` — Part 1: fiscal architecture, allocability, and budget-to-cash conversion.
- `papers/urban-demand-pressure-model.md` — Part 2: territorial demand, backlog risk, mobility stress, and spatial prioritisation.
- `papers/procurement-efficiency-capex-absorption.md` — Part 3: procurement structure, capital absorption, and intervention-performance review.
- `papers/causal-and-predictive-engine.md` — Part 4: dynamic panel modelling, forecasting, and fiscally admissible scenario design.
- `papers/budget-allocation-optimization-stack.md` — Part 5: mixed-integer budget allocation and intervention sequencing under legal and operational constraints.

## Python workflow

- `scripts/part1_fiscal_architecture.py` — execution and conversion metrics from annual-account data.
- `scripts/part2_urban_pressure.py` — pressure-scoring logic from tickets, incidents, and current works.
- `scripts/part3_procurement_capex.py` — procurement filtering and throughput summary for the mobility-maintenance perimeter.
- `scripts/part4_predictive_engine.py` — demand-panel preparation and negative-binomial modelling scaffold.
- `scripts/part5_optimization_stack.py` — portfolio optimization scaffold with budget floors, activation caps, and territorial coverage constraints.

## Data policy

This public GitHub version is **source-linked rather than data-bundled**.

To reproduce the analysis:
1. download the official Bologna files listed in `docs/source-catalog-and-download-guide.md`;
2. place them in `data/raw/` using the original filenames;
3. run the Python scripts locally.

This keeps the repository cleaner, lighter, and more prudent from a publication perspective while preserving full reproducibility.

## Suggested GitHub repository name

`bologna-operations-spending-efficiency-review`

## Suggested GitHub description

Consulting-style analytical repository on Bologna’s public finance, urban demand, procurement, forecasting, and optimization for roads, mobility, and urban maintenance.

## Suggested GitHub topics

`bologna`, `public-finance`, `procurement`, `urban-analytics`, `forecasting`, `optimization`, `public-sector`, `municipal-data`, `italy`, `consulting`

## Main documentation files

- `docs/source-catalog-and-download-guide.md` — official URLs, what each source contains, what it is used for, and how to download it.
- `docs/input-usage-audit.md` — exact audit of the Bologna input files used in the analytical work.
- `docs/publication-and-legal-notes.md` — practical GitHub publication note and attribution logic.
- `docs/repository-setup.md` — repository naming, positioning, and upload guidance.
- `docs/repository-manifest.md` — full file inventory of this GitHub-ready package.

## Copyright and reuse

The analytical text, synthesis, structure of indicators, and interpretive framework in this repository are original work. The repository does not grant any general open licence for full-text reuse. Reasonable excerpts may be quoted for research, teaching, academic discussion, or internal analytical use with clear attribution. Substantial reuse, adaptation, republication, or commercial use should credit the author and, where possible, request permission. Nothing in this repository constitutes legal advice.

4. Copyright and reuse

© 2025 Andrea Trenti. All rights reserved.
• The analytical texts, tables and structure of the indicators are original works protected by copyright.
• The underlying statistical data remain the property of their respective institutions (World Bank, IMF, industry associations, etc.) and are used exclusively for analytical and educational purposes.
• No open-source or Creative Commons licence is granted for the full reuse of the texts; any substantial reuse requires the author’s permission.
