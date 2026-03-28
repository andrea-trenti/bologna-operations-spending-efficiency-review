# Causal and Predictive Engine
## Dynamic panel modelling, hierarchical forecasting, and scenario design for Bologna’s urban-demand and execution pipeline

## Abstract

This note builds the predictive layer of the Bologna repository by integrating 12 municipal sources: the 2025–2027 budget, the 2025–2027 PEG, the 2024 annual account, two expenditure tables, the procurement archive, historical and current public-works registries, citizen tickets, traffic counts, public-transport validations, and incident statistics.[1][2][3][4][5][6][7][8][9][10][11][12] The purpose is not to produce a decorative forecast, but to construct a decision-grade engine linking territorial pressure, mobility exposure, programme-level fiscal constraints, and execution dynamics.

The data are already rich enough for a serious predictive architecture. The ticket database contains 119,083 observations from January 2017 to February 2026, equivalent to 110 monthly city observations and a balanced 72-month quartiere panel with 432 `month × quartiere` cells for 2019–2024.[9] Road-space-related tickets — urban degradation, traffic and viability, and street furniture — sum to 57,254, or 48.1% of the full ticket stock.[9] Traffic counts total 87.95 million passages over 2019–2024 on the measured corridor perimeter, with 2024 at 15.99 million and 2023–2024 growth of 12.5%.[10] Urban public-transport validations fell from 43.86 million in 2019 to 20.81 million in 2024, while urban service kilometres remained broadly stable at 17.97 million in 2019 and 17.48 million in 2024.[11] Incidents total 13,428 over 2018–2024, with 17,047 injuries and 123 deaths.[12]

## 1. Introduction

A city does not need forecasting because it wants elegant models. It needs forecasting because it must allocate scarce administrative and fiscal capacity before demand fully materialises. In Bologna’s case, this is particularly important because the previous papers established three facts: fiscal room is narrower than the headline budget suggests, procurement is count-fragmented and value-concentrated, and territorial demand is strongly peaked in a limited number of quartieri and corridors.[1][2][3][5][6][7][8][9][10][11][12]

## 2. Data and stylised facts

### 2.1 Predictive data stack

The repository already contains a sufficiently rich predictive stack.[1][2][3][4][5][6][7][8][9][10][11][12]

### 2.2 Ticket dynamics

The ticket archive contains 119,083 observations from January 2017 to February 2026.[9] By year, ticket counts are 12,697 in 2017, 13,613 in 2018, 13,927 in 2019, 12,758 in 2020, 11,889 in 2021, 13,367 in 2022, 13,452 in 2023, 12,909 in 2024, and 12,553 in 2025.[9] The road-space perimeter is large and persistent: road-related tickets total 57,254 over the sample.[9]

Seasonality is material. Across the full archive, September accumulates 12,245 tickets, June 11,587, October 11,446, and May 11,433, while December accumulates only 6,742 and August 7,944.[9]

### 2.3 Mobility, modal exposure, and safety as predictive covariates

Traffic and TPL data provide time-varying covariates plausibly linked to urban wear, congestion, exposure, and complaint generation. Traffic counts on the measured viali total 14.33 million in 2019, 12.93 million in 2020, 16.06 million in 2021, 14.42 million in 2022, 14.21 million in 2023, and 15.99 million in 2024.[10] Urban validations are 43.86 million in 2019 and 20.81 million in 2024.[11]

The incident layer supplies a severity proxy. Incidents total 2,022 in 2018, 1,942 in 2019, 1,319 in 2020, 1,921 in 2021, 2,120 in 2022, 2,158 in 2023, and 1,946 in 2024.[12]

### 2.4 Execution covariates and fiscal ceilings

The procurement file contains 26,467 procedures with €4.672 billion of base tender value, €3.478 billion of awarded value, and €2.310 billion of liquidated amounts.[6] The current works file contains 49 active works, of which 48, or 98.0%, fall in the road-space perimeter and 23, or 46.9%, are explicitly tram-related.[8]

At fiscal-programme level, the legal 2025 budget authorises €326.258 million for Mission 10, including €292.563 million for Programme 1002 and €33.292 million for Programme 1005.[1]

## 3. Framework

The natural starting point for road-space tickets is a negative-binomial panel:

$$
D_{i,t} \sim NB(\mu_{i,t}, k)
$$

$$
\log(\mu_{i,t}) = \alpha_i + \tau_t + \beta_1 \log(Inc_{i,t} + 1) + \beta_2 \log(Traf_t) + \beta_3 \log(TPL_t) + \beta_4 Works_{i,t-1} + \beta_5 Proc_{t-1} + \beta_6 Seas_t
$$

A separate execution model should be used for commitment and payment conversion:

$$
CCR_{p,t} = \frac{I_{p,t}}{CP_{p,t}}
$$

### Python implementation skeleton

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

tickets = pd.read_csv("data/raw/segnalazioni-open-citizen-relationship-management-czrm.csv", sep=";")
traffic = pd.read_csv("data/raw/traffico-viali.csv", sep=";")
tpl = pd.read_csv("data/raw/tpl_validazioni_km.csv", sep=";")
inc = pd.read_csv("data/raw/incidenti_new.csv", sep=";")
works_hist = pd.read_csv("data/raw/lavori-pubblici-storico.csv", sep=";")
```

## 4. Scenarios and analysis

### Scenario 1 — Conservative baseline

Total tickets are 12,909 in 2024 and 12,553 in 2025; road-space tickets are 6,364 in 2024 and 6,211 in 2025.[9] The two-year averages are therefore 12,731 total tickets and 6,288 road-space tickets.[9]

### Scenario 2 — Mobility-normalisation

Urban validations correlate with road-space tickets at 0.74 over 2019–2024, whereas the city-level traffic series do not show a similarly stable relationship.[9][10][11]

### Scenario 3 — Corridor-stress

At corridor level, concentration is extreme: Viale Panzacchi, Viale Pepoli, and Viale Filopanti alone absorb 63.6% of measured traffic, while the top five corridors absorb 89.4%.[10]

### Scenario 4 — Fiscal-execution scenario

Programme 1005 recorded €48.194 million of commitments and €37.044 million of competence payments in 2024, while the legal 2025 budget authorises €33.292 million.[1][3] That means the visible legal envelope is 30.9% below the prior-year commitment stock.[1][3]

## 5. Risks and caveats

The first caveat is identification. Tickets, incidents, traffic, and works are jointly determined to a meaningful extent. Works may reduce future complaints, but they can also generate short-run complaints through disruption.[7][8][9][10][12]

## 6. Comparison and implications

Most municipal dashboards report yesterday’s expenditure or yesterday’s complaints. Bologna’s data permit more. The predictive layer can estimate where the next complaint wave is likely to materialise, where corridor stress is building, and whether the visible budget-envelope can absorb the implied intervention need.[1][2][3][5][9][10][11][12]

## 7. Conclusion

Bologna already possesses the ingredients for a serious municipal predictive engine: 110 monthly ticket observations, a 72-month quartiere panel, annual incident and fiscal execution data, a dense procurement archive, public-works registries, and explicit legal budget ceilings.[1][2][3][5][6][7][8][9][10][11][12]

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
