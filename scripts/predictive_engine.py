"""Predictive Engine for the Bologna repository."""

from __future__ import annotations
from pathlib import Path
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

DATA = Path(__file__).resolve().parents[1] / "data" / "raw"
ROAD_CATS = {"Degrado urbano", "Viabilità e traffico", "Arredo urbano"}

def prepare_panel() -> pd.DataFrame:
    tickets = pd.read_csv(DATA / "segnalazioni-open-citizen-relationship-management-czrm.csv", sep=";")
    incidents = pd.read_csv(DATA / "incidenti_new.csv", sep=";")
    works_hist = pd.read_csv(DATA / "lavori-pubblici-storico.csv", sep=";")

    tickets["date"] = pd.to_datetime(tickets["Data inserimento"], utc=True, errors="coerce")
    tickets = tickets[(tickets["date"] >= "2019-01-01") & (tickets["date"] < "2025-01-01")].copy()
    tickets["year"] = tickets["date"].dt.year
    tickets["quartiere"] = tickets["Quartiere"].str.replace(" - ", "-", regex=False)
    tickets["road_ticket"] = tickets["Sottocategoria 1"].isin(ROAD_CATS).astype(int)

    tq = (
        tickets.groupby(["year", "quartiere"])
        .agg(road_tickets=("road_ticket", "sum"), tickets=("ID ticket", "count"))
        .reset_index()
    )

    incidents["quartiere"] = incidents["Quartiere"].str.replace(" - ", "-", regex=False)
    for c in ["Numero incidenti", "Totale feriti", "Totale morti"]:
        incidents[c] = pd.to_numeric(incidents[c], errors="coerce")

    inc = (
        incidents.groupby(["anno", "quartiere"])[["Numero incidenti", "Totale feriti", "Totale morti"]]
        .sum()
        .reset_index()
        .rename(columns={"anno": "year"})
    )

    hist = (
        works_hist.groupby(["Anno", "Quartiere - 1"])
        .size()
        .reset_index(name="hist_works")
        .rename(columns={"Anno": "year", "Quartiere - 1": "quartiere"})
    )
    hist["quartiere"] = hist["quartiere"].str.replace(" - ", "-", regex=False)

    panel = tq.merge(inc, on=["year", "quartiere"], how="left").merge(hist, on=["year", "quartiere"], how="left").fillna(0)
    return panel

def fit_model(panel: pd.DataFrame):
    model = smf.glm(
        "road_tickets ~ np.log1p(Numero incidenti) + np.log1p(hist_works) + C(quartiere) + C(year)",
        data=panel,
        family=sm.families.NegativeBinomial()
    ).fit()
    return model

if __name__ == "__main__":
    panel = prepare_panel()
    model = fit_model(panel)
    print(model.summary())
