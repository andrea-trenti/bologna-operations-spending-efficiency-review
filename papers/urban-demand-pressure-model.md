# Urban Demand Pressure Model
## Territorial backlog, mobility stress, and service-allocation risk in Bologna

## Abstract

This note develops a spatial-operational model of urban demand pressure in Bologna by integrating 12 municipal data assets: the 2025–2027 budget, the 2025–2027 PEG, the 2024 annual account, open-data expenditure tables, procurement records, public-works tables, citizen tickets, traffic counts, public-transport validations, and incident data.[1][2][3][4][5][6][7][8][9][10][11][12] The objective is not descriptive urban analytics, but a decision model: identify where Bologna’s service pressure is concentrated, where the backlog risk is structurally highest, and how a fiscally constrained municipality should prioritise maintenance and mobility interventions.

The core stylised facts are strong. The citizen-ticket database contains 119,083 records from 2017 to early 2026; the three largest ticket categories alone are urban degradation (24,233), traffic and viability (23,974), and environmental degradation (15,644), while road-space-related categories such as urban degradation, traffic/viability, and street furniture jointly account for 57,254 tickets, or 48.1% of the entire ticket stock.[9] Traffic counts cover 7,160 corridor-day observations from 2019 to early 2026, with cumulative totals concentrated on a handful of axes, notably Viale Panzacchi (24.9 million), Viale Pepoli (22.0 million), and Viale Filopanti (19.8 million).[10] Public-transport data cover 81 monthly records between 2019 and 2025, showing 43.9 million urban validations in 2019 versus 20.8 million in 2024.[11] Incident data cover 2018–2024 and report 13,428 incidents in total, of which 2,986 occurred in San Donato–San Vitale, 2,467 in Navile, and 2,282 in Porto–Saragozza.[12]

## 1. Introduction

Municipal service allocation often fails for a predictable reason: the city is managed through administrative compartments, while demand arrives spatially and cross-functionally. A pothole, a damaged curb, weak lighting, poor signage, traffic congestion, unsafe crossings, and repeated citizen complaints are not separate problems from the city’s point of view. They are different symptoms of the same territorial stress field.

## 2. Data and stylised facts

### 2.1 Data architecture

The analytical stack combines legal-financial documents, computable accounting tables, and spatial-operational datasets.[1][2][3][4][5][6][7][8][9][10][11][12]

| Source | Coverage | Observations | Analytical role |
|---|---:|---:|---|
| `Bilancio di Previsione 2025_2027.pdf` | 2025–2027 | official document | legal fiscal perimeter and mission-level appropriations [1] |
| `Piano esecutivo di gestione assestato 2025_2027.pdf` | 2025–2027 | official document | chapter-level earmarks and CDR logic [2] |
| `Rendiconto 2024.pdf` | 2024 | official document | annual-account structure, result of administration, SIOPE annexes [3] |
| `bilancio-di-previsione-previsione-uscite.csv` | 2013–2025 | 2,495 rows | computable 2025 budget structure [4] |
| `rendiconto-di-gestione-rendiconto-uscite.csv` | 2013–2024 | 3,334 rows | computable 2024 actual commitments/payments [5] |
| `gare-e-appalti.csv` | 2012–2026 | 26,467 procedures | procurement throughput and liquidity chain [6] |
| `lavori-pubblici-storico.csv` | historical | 1,536 works | historical supply footprint [7] |
| `lavori-pubblici.csv` | current | 49 works | current implementation stock [8] |
| `segnalazioni-open-citizen-relationship-management-czrm.csv` | 2017–2026 | 119,083 tickets | territorial demand and failure signals [9] |
| `traffico-viali.csv` | 2019–2026 | 7,160 rows | corridor traffic intensity [10] |
| `tpl_validazioni_km.csv` | 2019–2025 | 81 months | public-transport demand and service exposure [11] |
| `incidenti_new.csv` | 2018–2024 | 175 area-year rows | safety-risk layer [12] |

### 2.2 Demand concentration: tickets are not diffuse

The citizen-ticket database contains 119,083 observations from 2017 to early 2026.[9] Ticket volume is not evenly distributed across quartieri. Porto–Saragozza alone records 24,759 tickets, followed by Santo Stefano with 20,767, San Donato–San Vitale with 19,632, Borgo Panigale–Reno with 18,546, Navile with 18,443, and Savena with 16,932.[9] The top three quartieri therefore absorb 54.7% of all tickets, and the top five absorb 85.8%.[9]

Category concentration is equally important. The largest first-level categories are urban degradation (24,233), traffic and viability (23,974), environmental degradation (15,644), green maintenance (13,022), and street furniture (9,047).[9] A road-and-public-space perimeter defined as `urban degradation + traffic and viability + street furniture` totals 57,254 tickets, or 48.1% of the full database.[9]

### 2.3 Mobility and safety pressure

The traffic dataset contains 7,160 records from 2019 to early 2026 and measures daily totals on major viali and corridors.[10] Annual measured traffic totals were 14.33 million in 2019, 12.93 million in 2020, 16.06 million in 2021, 14.42 million in 2022, 14.27 million in 2023, and 15.99 million in 2024.[10] Relative to 2019, 2024 traffic was 11.6% higher on the measured perimeter.[10]

Public transport shows a different but equally relevant stress profile. Urban validations were 43.86 million in 2019, 19.60 million in 2020, 18.85 million in 2021, 19.94 million in 2022, 21.59 million in 2023, and 20.81 million in 2024.[11] Urban kilometres remained broadly stable by comparison, at 15.72 million in 2019, 14.85 million in 2020, 15.31 million in 2021, 15.06 million in 2022, 15.24 million in 2023, and 15.42 million in 2024.[11]

Safety risk is concentrated as well. The incident dataset reports 13,428 incidents between 2018 and 2024, with 17,047 injuries and 123 deaths across the same period.[12] Quartiere concentration is strong: San Donato–San Vitale records 2,986 incidents, Navile 2,467, Porto–Saragozza 2,282, Santo Stefano 2,245, Borgo Panigale–Reno 2,036, and Savena 1,412.[12]

### 2.4 Supply footprint: works are already road-heavy

The historical public-works file contains 1,536 works.[7] The largest first-level work types are paved road (`Strada bitumata`, 614), paved sidewalk (`Marciapiede bitumato`, 234), road (`Strada`, 218), stone road (`Strada lapidea`, 92), roadbed (`Sede stradale`, 28), bridge (`Ponte`, 22), and stone sidewalk (`Marciapiede lapideo`, 21).[7] A broad road-space perimeter captures 1,243 works, or 80.9% of the historical works stock.[7]

The current works file contains 49 ongoing works.[8] Of these, 31 are labelled `Strada`, 12 `Strada bitumata`, 4 `Marciapiede bitumato`, 1 `Pista ciclabile`, and 1 `Altro`, meaning that 48 of 49 ongoing works, or 98.0%, sit in the road-space perimeter.[8]

## 3. Framework

For each spatial unit $i$ and time period $t$, define:

- $D_{it}$ = citizen-demand signal (tickets);
- $S_{it}$ = safety signal (incidents / injuries);
- $M_{it}$ = mobility exposure (traffic and public-transport use);
- $W_{it}$ = realised work supply;
- $P_{it}$ = procurement and spending throughput;
- $B_{it}$ = latent backlog;
- $U_{it}$ = urban pressure index.

A simple reduced-form pressure metric is:

$$
U_{it} = \alpha z(D_{it}) + \beta z(S_{it}) + \gamma z(M_{it}) - \delta z(W_{it}) - \eta z(P_{it})
$$

### Python implementation skeleton

```python
import pandas as pd
import numpy as np

tickets = pd.read_csv("data/raw/segnalazioni-open-citizen-relationship-management-czrm.csv", sep=";")
incidents = pd.read_csv("data/raw/incidenti_new.csv", sep=";")
works_hist = pd.read_csv("data/raw/lavori-pubblici-storico.csv", sep=";")
works_cur = pd.read_csv("data/raw/lavori-pubblici.csv", sep=";")

tickets["Data inserimento"] = pd.to_datetime(tickets["Data inserimento"], utc=True, errors="coerce")
tickets["month"] = tickets["Data inserimento"].dt.to_period("M").astype(str)
road_cats = ["Degrado urbano", "Viabilità e traffico", "Arredo urbano"]
tickets["road_related"] = tickets["Sottocategoria 1"].isin(road_cats)
```

## 4. Scenarios and analysis

### Scenario 1 — Diffuse reactive allocation

The top three quartieri by combined significance—San Donato–San Vitale, Porto–Saragozza, and Navile—account for 52.8% of all tickets, 57.6% of incidents, 52.3% of road-related tickets, and 83.7% of ongoing works.[8][9][12] Under these conditions, diffuse allocation almost certainly over-serves low-pressure territory and under-serves the dominant stress nodes.

### Scenario 2 — Quartiere-targeted pressure management

A more rational regime would explicitly rank quartieri by a composite pressure score. A simple first-pass quartiere ranking built on tickets, incidents, and inverse work density places San Donato–San Vitale first, followed by Porto–Saragozza, Navile, Borgo Panigale–Reno, Santo Stefano, and Savena.[7][8][9][12]

### Scenario 3 — Corridor-first road and signage strategy

The top three measured traffic axes—Viale Panzacchi, Viale Pepoli, and Viale Filopanti—carry 63.6% of total measured traffic; the top five rise to 89.4%.[10] If road-surface quality, signage integrity, lane readability, curb design, lighting, and crossing safety are even modestly related to traffic load, then corridor-first prioritisation will dominate uniform network treatment.

### Scenario 4 — Fiscally bounded prioritisation

In the 2025 computable budget, Mission 10 totals €251.8 million and Programme 1005 (`Viabilità e infrastrutture stradali`) €35.8 million.[4] In the 2024 annual account, Mission 10 commitments were €178.9 million and Programme 1005 commitments €48.2 million.[5] The constrained optimisation problem is therefore not trivial.

## 5. Risks and caveats

The first caveat is reporting bias in citizen tickets. Complaint data are a valuable demand signal, but not a complete welfare measure. Some areas report more intensively than others, and some defects remain under-reported.[9]

## 6. Comparison and implications

For municipal operators, the immediate implication is that a road-space and mobility control tower is analytically justified. Nearly half of all tickets are already in the physical-city perimeter; ongoing works are almost entirely road-related; procurement in the same perimeter is economically material; and mobility/safety signals are strongly concentrated.[6][7][8][9][10][11][12]

## 7. Conclusion

Bologna’s urban pressure is not diffuse. It is concentrated across a relatively small set of quartieri, proximity zones, and traffic corridors. The empirical evidence is clear: 119,083 tickets since 2017, 57,254 road-space-related tickets, 13,428 incidents since 2018, 1,536 historical public works, 49 ongoing works of which 48 are road-related, 26,467 procurement records, and traffic intensity dominated by a handful of viali.[6][7][8][9][10][12]

## References

[1] Comune di Bologna — *Bilancio di Previsione 2025_2027*, 2025, official budget document (PDF).
[2] Comune di Bologna — *Piano esecutivo di gestione assestato 2025_2027*, 2025, official PEG document (PDF).
[3] Comune di Bologna — *Rendiconto 2024*, 2024, official annual account document (PDF).
[4] Comune di Bologna Open Data — *bilancio-di-previsione-previsione-uscite.csv*, 2013–2025, municipal open-data dataset.
[5] Comune di Bologna Open Data — *rendiconto-di-gestione-rendiconto-uscite.csv*, 2013–2024, municipal open-data dataset.
[6] Comune di Bologna Open Data — *gare-e-appalti.csv*, 2012–2026, procurement dataset.
[7] Comune di Bologna Open Data — *lavori-pubblici-storico.csv*, historical public-works dataset.
[8] Comune di Bologna Open Data — *lavori-pubblici.csv*, ongoing public-works dataset.
[9] Comune di Bologna Open Data — *segnalazioni-open-citizen-relationship-management-czrm.csv*, citizen-ticket dataset, 2017–2026.
[10] Comune di Bologna Open Data — *traffico-viali.csv*, traffic dataset, 2019–2026.
[11] Comune di Bologna Open Data — *tpl_validazioni_km.csv*, public-transport validations and kilometres dataset, 2019–2025.
[12] Comune di Bologna Open Data — *incidenti_new.csv*, incident dataset, 2018–2024.
[13] Repubblica Italiana — *Decreto legislativo 23 giugno 2011, n. 118*, harmonised accounting framework for territorial entities, law.
[14] Repubblica Italiana — *Decreto legislativo 18 agosto 2000, n. 267 (TUEL)*, local-authority legal framework, law.
