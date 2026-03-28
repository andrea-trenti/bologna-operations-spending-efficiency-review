# Bologna Operations and Spending Efficiency Review

This repository contains a structured analysis of the **Comune di Bologna** focused on public finance, urban demand, procurement, forecasting, and intervention design for roads, mobility, and urban maintenance.

The project was developed as an independent research effort driven by interest in Bologna as a city and in the mechanics of municipal decision-making. The objective is not to publish raw municipal files indiscriminately, but to present a coherent analytical body of work built on official documents and open data, together with the code needed to reconstruct the main steps locally.

## What is in the repository

- six Markdown papers forming one continuous analytical sequence;
- five Python scripts reproducing the main quantitative steps;
- a source guide with official links and download instructions;
- a reproducibility note explaining how to rebuild the local workflow;
- publication and attribution notes for a clean public repository.

## Repository structure

- `papers/` — main analytical texts.
- `scripts/` — Python scripts corresponding to the main analytical workflow.
- `docs/` — source guide, input audit, reproducibility note, publication note, and project structure.
- `requirements.txt` — Python dependencies.
- `.gitignore` — excludes local data downloads and cache files.

## Papers

- `papers/bologna-context-and-motivation.md` — Bologna as the civic and analytical setting of the project.
- `papers/municipal-fiscal-architecture-cash-conversion.md` — fiscal architecture, allocability, and budget-to-cash conversion.
- `papers/urban-demand-pressure-model.md` — territorial demand, backlog risk, mobility stress, and spatial prioritisation.
- `papers/procurement-efficiency-capex-absorption.md` — procurement structure, capital absorption, and intervention-performance review.
- `papers/causal-and-predictive-engine.md` — dynamic panel modelling, forecasting, and fiscally admissible scenario design.
- `papers/budget-allocation-optimization-stack.md` — mixed-integer budget allocation and intervention sequencing under legal and operational constraints.

## Scripts

- `scripts/fiscal_architecture.py` — execution and conversion metrics from annual-account data.
- `scripts/urban_pressure.py` — quartiere-level pressure scoring from complaints, incidents, and current works.
- `scripts/procurement_capex.py` — procurement filtering and throughput summary for the mobility-maintenance perimeter.
- `scripts/predictive_engine.py` — demand-panel preparation and negative-binomial modelling scaffold.
- `scripts/optimization_stack.py` — portfolio optimisation scaffold with budget floors, activation caps, and territorial coverage constraints.

## Sources and replication

No raw municipal files are included in this repository. Official sources, expected filenames, and download links are documented in `docs/data-sources.md`.  
To reproduce the analysis locally:

1. download the files listed in `docs/data-sources.md`;
2. place them in `data/raw/` using the original filenames;
3. install the dependencies in `requirements.txt`;
4. run the scripts from the repository root.

## Recommended repository name

`bologna-operations-spending-efficiency-review`

## Suggested description

Consulting-style analytical repository on Bologna’s public finance, urban demand, procurement, forecasting, and optimisation for roads, mobility, and urban maintenance.

## Main documentation files

- `docs/data-sources.md` — official URLs, what each source contains, and what it is used for.
- `docs/input-audit.md` — exact audit of the Bologna files used in the project.
- `docs/reproducibility.md` — local setup and execution notes.
- `docs/publication-notes.md` — publication and attribution note.
- `docs/project-structure.md` — full repository tree and file descriptions.

## Copyright and reuse

The analytical text, synthesis, structure of indicators, and interpretive framework in this repository are original work. The repository does not grant any general open licence for full-text reuse. Reasonable excerpts may be quoted for research, teaching, academic discussion, or internal analytical use with clear attribution. Substantial reuse, adaptation, republication, or commercial use should credit the author and, where possible, request permission. Nothing in this repository constitutes legal advice.

© 2026 Andrea Trenti. All rights reserved.
• The analytical texts, tables and structure of the indicators are original works protected by copyright.
• The underlying statistical data remain the property of their respective institutions (World Bank, IMF, industry associations, etc.) and are used exclusively for analytical and educational purposes.
• No open-source or Creative Commons licence is granted for the full reuse of the texts; any substantial reuse requires the author’s permission.
