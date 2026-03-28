# Python Workflow

The repository contains five Python scripts corresponding to the five analytical steps.

## Scripts

- `scripts/part1_fiscal_architecture.py`
  - computes execution and conversion metrics from the annual-account data.

- `scripts/part2_urban_pressure.py`
  - builds quartiere-level pressure scores using complaints, incidents, and current works.

- `scripts/part3_procurement_capex.py`
  - filters and summarises the mobility-maintenance procurement perimeter.

- `scripts/part4_predictive_engine.py`
  - prepares the quartiere-year panel and estimates a negative-binomial model scaffold.

- `scripts/part5_optimization_stack.py`
  - builds the optimization-ready panel and solves a basic portfolio allocation model.

## Expected local data path

All scripts expect the official source files to be placed in:

```text
data/raw/
```

using the filenames documented in `docs/source-catalog-and-download-guide.md`.
