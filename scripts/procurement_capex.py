"""Procurement Capex for the Bologna repository."""

from __future__ import annotations
from pathlib import Path
import pandas as pd
import re

DATA = Path(__file__).resolve().parents[1] / "data" / "raw"

KEYWORDS = [
    "strad", "viabil", "segnalet", "marciapied", "ponte",
    "ciclab", "tram", "tpl", "mobilit", "asfalto", "illumin"
]

def load_procurement() -> pd.DataFrame:
    ga = pd.read_csv(DATA / "gare-e-appalti.csv", sep=";", low_memory=False)
    for c in [
        "Importo appalto (Euro)",
        "Importo di aggiudicazione (Euro)",
        "Importo delle somme liquidate (Euro)",
    ]:
        ga[c] = pd.to_numeric(ga[c], errors="coerce")
    return ga

def mobility_subset(ga: pd.DataFrame) -> pd.DataFrame:
    text_cols = [c for c in ga.columns if ga[c].dtype == "object"]
    pattern = re.compile("|".join(KEYWORDS), flags=re.IGNORECASE)
    mask = pd.Series(False, index=ga.index)
    for c in text_cols:
        mask = mask | ga[c].fillna("").str.contains(pattern)
    return ga[mask].copy()

def main():
    ga = load_procurement()
    sub = mobility_subset(ga)
    out = {
        "proc_count_all": len(ga),
        "award_all": ga["Importo di aggiudicazione (Euro)"].sum(),
        "proc_count_mobility": len(sub),
        "award_mobility": sub["Importo di aggiudicazione (Euro)"].sum(),
        "liq_mobility": sub["Importo delle somme liquidate (Euro)"].sum(),
    }
    print(out)

if __name__ == "__main__":
    main()
