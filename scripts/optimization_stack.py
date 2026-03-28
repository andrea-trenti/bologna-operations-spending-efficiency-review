"""Optimization Stack for the Bologna repository."""

from __future__ import annotations
from pathlib import Path
import pandas as pd
import numpy as np
import pulp as pl

DATA = Path(__file__).resolve().parents[1] / "data" / "raw"
ROAD_CATS = {"Degrado urbano", "Viabilità e traffico", "Arredo urbano"}

def z(s: pd.Series) -> pd.Series:
    s = s.astype(float)
    std = s.std(ddof=0)
    if std == 0:
        return pd.Series(0.0, index=s.index)
    return (s - s.mean()) / std

def build_panel() -> pd.DataFrame:
    tickets = pd.read_csv(DATA / "segnalazioni-open-citizen-relationship-management-czrm.csv", sep=";")
    inc = pd.read_csv(DATA / "incidenti_new.csv", sep=";")
    works_cur = pd.read_csv(DATA / "lavori-pubblici.csv", sep=";")

    tickets["quartiere"] = tickets["Quartiere"].str.replace(" - ", "-", regex=False)
    inc["quartiere"] = inc["Quartiere"].str.replace(" - ", "-", regex=False)
    works_cur["quartiere"] = works_cur["Quartiere - 1"].str.replace(" - ", "-", regex=False)

    tickets["road_ticket"] = tickets["Sottocategoria 1"].isin(ROAD_CATS).astype(int)
    road = tickets.groupby("quartiere")["road_ticket"].sum().rename("road_tickets")
    incq = inc.groupby("quartiere")["Numero incidenti"].sum().rename("incidents")
    curw = works_cur.groupby("quartiere").size().rename("current_works")

    panel = pd.concat([road, incq, curw], axis=1).fillna(0)
    panel["under_coverage"] = (
        (panel["road_tickets"] / panel["road_tickets"].sum()) -
        (panel["current_works"] / max(panel["current_works"].sum(), 1))
    )
    panel["pressure"] = (
        0.35 * z(panel["road_tickets"]) +
        0.30 * z(panel["incidents"]) +
        0.20 * z(panel["under_coverage"]) +
        0.15 * z(panel["road_tickets"] / (panel["current_works"] + 1))
    )
    return panel

def solve_portfolio(panel: pd.DataFrame):
    quartieri = panel.index.tolist()
    packages = {
        "routine_road":  {"cost": 0.25, "relief": 1.0, "admin": 1, "disruption": 1},
        "signage":       {"cost": 0.05, "relief": 0.45, "admin": 1, "disruption": 0},
        "sidewalk":      {"cost": 0.18, "relief": 0.75, "admin": 1, "disruption": 1},
        "safety_hotspot":{"cost": 0.40, "relief": 1.35, "admin": 2, "disruption": 1},
        "corridor_major":{"cost": 1.20, "relief": 3.20, "admin": 3, "disruption": 3},
    }

    model = pl.LpProblem("Bologna_Portfolio", pl.LpMaximize)
    x = pl.LpVariable.dicts(
        "x", ((i, k) for i in quartieri for k in packages.keys()),
        lowBound=0, upBound=1, cat="Binary"
    )

    model += pl.lpSum(
        (panel.loc[i, "pressure"] * packages[k]["relief"]
         - 0.10 * packages[k]["disruption"]
         - 0.05 * packages[k]["admin"]) * x[(i, k)]
        for i in quartieri for k in packages.keys()
    )

    model += pl.lpSum(packages[k]["cost"] * x[(i, k)] for i in quartieri for k in packages.keys()) <= 33.292
    capex_like = ["routine_road", "sidewalk", "safety_hotspot", "corridor_major"]
    model += pl.lpSum(packages[k]["cost"] * x[(i, k)] for i in quartieri for k in capex_like) <= 25.813
    model += pl.lpSum(packages["routine_road"]["cost"] * x[(i, "routine_road")] for i in quartieri) >= 2.632
    model += pl.lpSum(packages["signage"]["cost"] * x[(i, "signage")] for i in quartieri) >= 0.120
    for q in [q for q in quartieri if q in {"Savena", "Santo Stefano"}]:
        model += pl.lpSum(x[(q, k)] for k in packages.keys()) >= 1
    model += pl.lpSum(packages[k]["admin"] * x[(i, k)] for i in quartieri for k in packages.keys()) <= 230

    model.solve(pl.PULP_CBC_CMD(msg=False))
    selected = [(i, k) for i in quartieri for k in packages.keys() if x[(i, k)].value() and x[(i, k)].value() > 0.5]
    return selected

if __name__ == "__main__":
    panel = build_panel()
    print(solve_portfolio(panel))
