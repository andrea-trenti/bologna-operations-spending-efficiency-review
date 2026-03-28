# Reproducibility

## Local setup

Create the following local structure next to the repository contents:

```text
data/
  raw/
```

Download the official source files listed in `docs/data-sources.md` and place them in `data/raw/` with the exact filenames shown there.

## Python environment

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Scripts

Run the scripts from the repository root.

- `python scripts/fiscal_architecture.py`
- `python scripts/urban_pressure.py`
- `python scripts/procurement_capex.py`
- `python scripts/predictive_engine.py`
- `python scripts/optimization_stack.py`

## Script roles

- `fiscal_architecture.py` computes execution and conversion ratios from the annual-account data.
- `urban_pressure.py` builds quartiere-level pressure scores from tickets, incidents, and current works.
- `procurement_capex.py` filters and summarises the mobility-maintenance procurement perimeter.
- `predictive_engine.py` prepares a quartiere-year panel and estimates a negative-binomial scaffold.
- `optimization_stack.py` builds the optimisation panel and solves a constrained portfolio-selection model.

## Notes

The scripts are intentionally compact and readable. They are designed to mirror the logic of the papers rather than to act as a full production pipeline.
