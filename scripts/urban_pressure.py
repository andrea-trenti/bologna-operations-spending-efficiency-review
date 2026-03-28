"""Urban Pressure for the Bologna repository."""

from __future__ import annotations
from pathlib import Path
import pandas as pd
import numpy as np

DATA = Path(__file__).resolve().parents[1] / "data" / "raw"
ROAD_CATS = {"Degrado urbano", "Viabilità e traffico", "Arredo urbano"}

def z(s: pd.Series) -> pd.Series:
    s = s.astype(float)
    std = s.std(ddof=0)
    if std == 0:
        return pd.Series(0.0, index=s.index)
    return (s - s.mean()) / std

def build_pressure_table() -> pd.DataFrame:
    tickets = pd.read_csv(DATA / "segnalazioni-open-citizen-relationship-management-czrm.csv", sep=";")
    incidents = pd.read_csv(DATA / "incidenti_new.csv", sep=";")
    works_cur = pd.read_csv(DATA / "lavori-pubblici.csv", sep=";")

    tickets["quartiere"] = tickets["Quartiere"].str.replace(" - ", "-", regex=False)
    incidents["quartiere"] = incidents["Quartiere"].str.replace(" - ", "-", regex=False)
    works_cur["quartiere"] = works_cur["Quartiere - 1"].str.replace(" - ", "-", regex=False)

    tickets["road_ticket"] = tickets["Sottocategoria 1"].isin(ROAD_CATS).astype(int)

    road = tickets.groupby("quartiere")["road_ticket"].sum().rename("road_tickets")
    inc = incidents.groupby("quartiere")["Numero incidenti"].sum().rename("incidents")
    curw = works_cur.groupby("quartiere").size().rename("current_works")

    panel = pd.concat([road, inc, curw], axis=1).fillna(0)
    panel["under_coverage"] = (
        (panel["road_tickets"] / panel["road_tickets"].sum()) -
        (panel["current_works"] / max(panel["current_works"].sum(), 1))
    )
    panel["pressure_score"] = (
        0.45 * z(panel["road_tickets"]) +
        0.35 * z(panel["incidents"]) +
        0.20 * z(panel["under_coverage"])
    )
    return panel.sort_values("pressure_score", ascending=False)

if __name__ == "__main__":
    print(build_pressure_table())
