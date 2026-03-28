"""Fiscal Architecture for the Bologna repository."""

from __future__ import annotations
from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data" / "raw"

def load_data():
    bil = pd.read_csv(DATA / "bilancio-di-previsione-previsione-uscite.csv")
    ren = pd.read_csv(DATA / "rendiconto-di-gestione-rendiconto-uscite.csv", sep=";")
    return bil, ren

def compute_fiscal_metrics():
    _, ren = load_data()
    ren24 = ren[ren["Anno"] == 2024].copy()
    oper = ren24[~ren24["Missione"].isin([60, 99])].copy()

    cp = oper["Previsioni definitive di competenza"].sum()
    imp = oper["Impegni"].sum()
    pc = oper["Pagamenti in c/competenza"].sum()
    fpv = oper["Fondo pluriennale vincolato"].sum()
    rs = oper["Residui passivi a inizio anno"].sum()
    pr = oper["Pagamenti in c/residui"].sum()
    r = oper["Riaccertamenti residui"].sum()

    ep = rs - pr + r
    ec = imp - pc

    out = {
        "commitment_conversion_ratio": imp / cp if cp else None,
        "payment_on_commitment_ratio": pc / imp if imp else None,
        "fpv_intensity": fpv / cp if cp else None,
        "residual_carry_over_ratio": (ep + ec) / imp if imp else None,
    }
    return out

if __name__ == "__main__":
    metrics = compute_fiscal_metrics()
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")
