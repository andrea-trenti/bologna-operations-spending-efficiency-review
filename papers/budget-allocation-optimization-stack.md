# Budget Allocation and Optimization Stack
## Mixed-integer intervention design for Bologna’s roads, mobility, and urban-maintenance portfolio

## Abstract

This note develops the final decision layer of the Bologna repository: a mathematically explicit optimization stack linking territorial pressure, fiscal admissibility, procurement throughput, and intervention sequencing.[1][2][3][4][5][6][7][8][9][10][11][12] The purpose is not to produce a generic ranking of neighbourhoods, but to specify how a municipality with legally constrained resources should choose which interventions to fund, where to place them, when to sequence them, and under which administrative and procurement constraints.

The empirical context is strong enough for optimization. Bologna’s legal 2025 budget authorises €326.258 million for Mission 10 `Trasporti e diritto alla mobilità`, of which €292.563 million sit in Programme 1002 `Trasporto pubblico locale` and €33.292 million in Programme 1005 `Viabilità e infrastrutture stradali`.[1] The 2024 annual account records €130.325 million of commitments and €99.766 million of competence payments for Programme 1002, and €48.194 million of commitments and €37.044 million of competence payments for Programme 1005.[3] In the computable annual-account table, the 2024 Title-2 commitment-conversion ratio is only 23.4% for Programme 1002 and 35.5% for Programme 1005, while FPV intensity is 13.9% and 36.8% respectively.[5] The system therefore faces a classic public-sector optimization problem: the legally visible budget is not the same thing as executable capital capacity.[1][3][5]

The pressure side is equally concentrated. The ticket database contains 119,083 observations from 2017 to early 2026, of which 57,254, or 48.1%, are road-space related.[9] Porto-Saragozza alone accounts for 12,848 road-space tickets, Santo Stefano 10,933, Savena 8,770, San Donato-San Vitale 8,735, Navile 8,350, and Borgo Panigale-Reno 7,617.[9] The incident file records 13,428 incidents from 2018 to 2024, with 2,986 in San Donato-San Vitale, 2,467 in Navile, 2,282 in Porto-Saragozza, 2,245 in Santo Stefano, 2,036 in Borgo Panigale-Reno, and 1,412 in Savena.[12]

## 1. Introduction

Optimization is often the weakest part of public-sector analytics because it is treated either as a toy model or as a black box disconnected from legal and accounting reality. That approach is especially unsuitable for Bologna. The previous papers showed that fiscal room is constrained, demand is spatially concentrated, procurement is count-fragmented and value-concentrated, and execution bottlenecks are more binding than nominal appropriations.[1][2][3][5][6][7][8][9][10][11][12]

## 2. Data and stylised facts

### 2.1 Hard fiscal and execution boundaries

The legal 2025 budget sets the first boundary. Mission 10 totals €326.258 million, with €292.563 million in Programme 1002 and €33.292 million in Programme 1005.[1] Mission 09 totals €103.328 million and Mission 08 €53.190 million, creating adjacent but distinct envelopes for environmental and territorial actions.[1]

The annual account sets the second boundary. Programme 1005 records €48.194 million of 2024 commitments and €37.044 million of competence payments, while Programme 1002 records €130.325 million of commitments and €99.766 million of competence payments.[3]

Within Title 2, Programme 1005 shows €72.682 million of definitive competence appropriations, €25.813 million of commitments, €19.754 million of competence payments, and €26.737 million of FPV in 2024.[5] Programme 1002 shows €529.748 million of appropriations, €124.059 million of commitments, €94.371 million of competence payments, and €73.799 million of FPV.[5]

### 2.2 Pressure concentration and under-coverage

Road-space tickets total 57,254 and are distributed as follows: Porto-Saragozza 12,848, Santo Stefano 10,933, Savena 8,770, San Donato-San Vitale 8,735, Navile 8,350, and Borgo Panigale-Reno 7,617.[9]

Among 43 ongoing works with identified quartiere, Porto-Saragozza has 13, San Donato-San Vitale 13, Navile 10, Borgo Panigale-Reno 4, Santo Stefano 3, and Savena 0.[8] Comparing current-works shares to road-ticket shares yields territorial saturation ratios of approximately 1.35 for Porto-Saragozza, 1.97 for San Donato-San Vitale, 1.60 for Navile, 0.70 for Borgo Panigale-Reno, 0.37 for Santo Stefano, and 0.00 for Savena.[8][9]

### 2.3 Procurement throughput and handling-capacity priors

The mobility-maintenance subset contains 2,453 procedures, €1.531 billion of base tender value, €1.215 billion of awarded value, and €723.639 million of liquidations.[6] Within that subset, direct awards account for 1,775 procedures and €361.277 million of awarded value, open procedures for 91 procedures and €641.438 million, and negotiated procedures for 399 procedures and €209.764 million.[6]

## 3. Framework

### 3.1 Decision units

Let:

- $i \in I$ index territorial units (quartieri or corridors);[8][9][10][12]
- $k \in K$ index intervention packages;
- $t \in T$ index planning periods;
- $p \in P$ index funding buckets.[1][2][3][5]

### 3.2 Parameters

For each unit $i$, package $k$, and period $t$, define:

- $u_i$ = road-ticket pressure score;[9]
- $r_i$ = incident-risk score;[12]
- $m_i$ = mobility criticality score from traffic and TPL exposure;[10][11]
- $h_i$ = under-coverage score from current-work saturation;[8][9]
- $g_{ik}$ = expected pressure relief if package $k$ is applied in unit $i$;[7][8][9][12]

Pressure weights can be normalised from observed shares:

$$
\pi_i = \alpha z(u_i) + \beta z(r_i) + \gamma z(m_i) + \delta z(h_i)
$$

### 3.3 Objective function

A useful mixed-integer linear formulation is:

$$
\min \sum_{t \in T} \left[
\sum_{i \in I} \left( \omega_1 b_{it} + \omega_2 r_i b_{it} + \omega_3 m_i b_{it} \right)
+ \sum_{i,k} \omega_4 d_{ik} x_{ikt}
+ \sum_j \omega_5 y_{jt}
\right]
$$

### 3.4 Constraint system

Key constraints are:

- legal budget constraints by programme/chapter;[1][2]
- historical activation constraints using 2024 Title-2 conversion ceilings;[5]
- chapter floors for routine maintenance and signage from the PEG;[2]
- administrative handling-capacity constraints using recent procedure counts;[6]
- disruption constraints on already stressed corridors;[8][10][11]
- territorial fairness floors for structurally under-covered zones.[8][9]

### Python implementation skeleton

```python
import pandas as pd
import numpy as np
import pulp as pl

tickets = pd.read_csv("data/raw/segnalazioni-open-citizen-relationship-management-czrm.csv", sep=";")
inc = pd.read_csv("data/raw/incidenti_new.csv", sep=";")
works_cur = pd.read_csv("data/raw/lavori-pubblici.csv", sep=";")
```

```python
quartieri = ["Porto-Saragozza","Santo Stefano","Savena","San Donato-San Vitale","Navile","Borgo Panigale-Reno"]
packages = {
    "routine_road":  {"cost": 0.25, "relief": 1.0, "admin": 1, "disruption": 1},
    "signage":       {"cost": 0.05, "relief": 0.45, "admin": 1, "disruption": 0},
    "sidewalk":      {"cost": 0.18, "relief": 0.75, "admin": 1, "disruption": 1},
    "safety_hotspot":{"cost": 0.40, "relief": 1.35, "admin": 2, "disruption": 1},
    "corridor_major":{"cost": 1.20, "relief": 3.20, "admin": 3, "disruption": 3},
}
```

## 4. Scenarios and analysis

### Scenario 1 — Baseline legal-feasible portfolio

In the baseline scenario, the optimizer respects the legal 2025 Programme 1005 envelope of €33.292 million and the historical 2024 Programme 1005 Title-2 activation ceiling of €25.813 million.[1][5] It also respects a routine-maintenance floor of €2.632 million from `U33500-000` and a signage floor of €119,840 from `U33460-000`.[2]

### Scenario 2 — Fiscal-stress scenario

In a stress scenario, the city applies a 10% prudential reduction to the visible Programme 1005 allocation available for discretionary optimization, leaving approximately €29.963 million instead of €33.292 million.[1] At the same time, procurement handling capacity is reduced from a baseline of 230 to 200 procedure-equivalent units to reflect tighter administrative bandwidth.[6]

### Scenario 3 — Activation-acceleration scenario

If Programme 1005 Title-2 commitment-conversion rises from 35.5% to 45.0%, additional activated capital equals:

$$
\Delta I_{1005} = 72.682 \times (0.450 - 0.355) \approx 6.90 \text{ million euro}
$$

If Programme 1002 Title-2 commitment-conversion rises from 23.4% to 30.0%, additional activated capital equals approximately €34.96 million.[5]

### Scenario 4 — Pressure-proportional rebalance

Among the 43 ongoing works with identified quartiere, a simple pressure-proportional benchmark based on road-ticket shares would allocate approximately 9.6 works to Porto-Saragozza, 8.2 to Santo Stefano, 6.6 to Savena, 6.5 to San Donato-San Vitale, 6.3 to Navile, and 5.7 to Borgo Panigale-Reno.[8][9] Actual allocation is 13, 3, 0, 13, 10, and 4 respectively.[8]

### Scenario 5 — Corridor-critical strategy

Viale Panzacchi, Viale Pepoli, and Viale Filopanti alone account for 63.6% of measured traffic, and the top five corridors account for 89.4%.[10] A corridor-critical scenario increases the weight on mobility criticality and tightens disruption caps.

## 5. Risks and caveats

The first caveat is unit-cost identification. The open datasets do not provide a perfect asset-level cost curve for every maintenance or safety package.[2][6][7][8] The optimizer must therefore begin with calibrated proxies.

## 6. Comparison and implications

A dashboard can rank quartieri by tickets. It cannot decide whether a city should fund signage in Savena, resurfacing in Porto-Saragozza, or a hotspot safety package in Navile given legal chapter floors, activation limits, current workstock, and procurement handling capacity.[1][2][5][6][8][9][12] That is the unique value of the optimization stack.

## 7. Conclusion

Bologna’s final problem is not data scarcity and not lack of fiscal documentation. It is the conversion of a legally constrained budget into a territorially rational intervention portfolio. The city’s 2025 visible road-infrastructure envelope is €33.292 million; its 2024 Programme 1005 Title-2 activated capital was €25.813 million; its current routine-maintenance floor is €2.632 million; its road-space complaint stock is 57,254; and its current workstock is heavily concentrated.[1][2][5][8][9]

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
[13] Repubblica Italiana — *Codice dei contratti pubblici (D.Lgs. 36/2023)*, public-procurement legal framework.
[14] Repubblica Italiana — *D.Lgs. 118/2011* and *D.Lgs. 267/2000 (TUEL)*, harmonised local-public-finance framework.
