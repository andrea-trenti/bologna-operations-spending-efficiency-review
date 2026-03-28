# Project Structure

```text
bologna-operations-spending-efficiency-review/
├── README.md
├── requirements.txt
├── .gitignore
├── papers/
│   ├── bologna-context-and-motivation.md
│   ├── municipal-fiscal-architecture-cash-conversion.md
│   ├── urban-demand-pressure-model.md
│   ├── procurement-efficiency-capex-absorption.md
│   ├── causal-and-predictive-engine.md
│   └── budget-allocation-optimization-stack.md
├── scripts/
│   ├── fiscal_architecture.py
│   ├── urban_pressure.py
│   ├── procurement_capex.py
│   ├── predictive_engine.py
│   └── optimization_stack.py
└── docs/
    ├── data-sources.md
    ├── input-audit.md
    ├── reproducibility.md
    ├── publication-notes.md
    └── project-structure.md
```

## File summary

### Root
- `README.md` — repository landing page.
- `requirements.txt` — Python dependencies.
- `.gitignore` — excludes local downloads and cache files.

### `papers/`
- introductory note on Bologna;
- fiscal architecture and cash-conversion analysis;
- urban demand-pressure model;
- procurement and capex-absorption review;
- predictive engine;
- optimisation stack.

### `scripts/`
- one script for each major quantitative block of the project.

### `docs/`
- official source guide;
- audit of the Bologna files used;
- local setup and reproducibility note;
- publication note;
- repository tree and file descriptions.
