# Municipal Fiscal Architecture and Cash-Conversion Review
## Bologna’s 2025–2027 budget, 2024 annual account, and the operational limits of allocable spending

## Abstract

This note examines the fiscal architecture of the Comune di Bologna through an integrated reading of the 2025–2027 budget, the 2025–2027 PEG, the 2024 annual account, and the municipal open-data layer on expenditure, procurement, public works, citizen tickets, traffic, public transport, and incidents [1][2][3][4][5][6][7][8][9][10][11][12]. The central question is not whether Bologna has a large budget in headline terms, but how much of that budget is legally allocable, operationally executable, and cash-convertible within the annual cycle [1][2][3][13][14].

The main finding is that Bologna’s headline fiscal scale materially overstates its truly discretionary room. The 2025 comprehensive expenditure envelope is €1.528 billion, but current expenditure alone absorbs €696.334 million, while Titles 1–3 revenues amount to €706.546 million, leaving a current-balance cushion of only €10.212 million before debt repayment and a slightly negative margin after scheduled debt service [1]. The 2024 result of administration is €340.737 million, yet only €32.711 million is freely available because €224.066 million are accantonamenti, €79.609 million are vincoli, and €4.351 million are already destined to investments [3]. This implies that only 9.6% of the reported administration result is genuinely discretionary [3].

The second finding is that Bologna’s core bottleneck is not merely fiscal scarcity but conversion efficiency: appropriations are not equivalent to activated spending, and activated spending is not equivalent to cash execution. In the 2024 open-data annual account, the operating perimeter excluding treasury advances and third-party flows shows a commitment-conversion ratio of 46.8%, a payment-on-commitment ratio of 79.3%, an FPV intensity of 15.0%, and a residual carry-over ratio of 22.5% [5]. The most consequential inefficiency therefore lies in execution sequencing, capital absorption, earmark complexity, and chapter-level cash conversion rather than in the absence of nominal resources [2][3][5].

## 1. Introduction

A municipal budget can be large in legal-appropriation terms and still be tight in allocable, executable, and liquid terms. This distinction is particularly relevant in Italian local public finance, where the harmonised accounting framework under D.Lgs. 118/2011 and the equilibrium discipline of the TUEL require analysts to distinguish among competence appropriations, commitments, payments, residuals, earmarked resources, the fondo pluriennale vincolato, and the result of administration [3][13][14]. For management, consulting, and policy work, this is not a technicality: it determines whether “more spending” is feasible, which programmes are truly flexible, and where process reform can substitute for additional resources [1][2][3].

Bologna is a strong case study because its fiscal documentation is unusually rich and can be linked to a deep operational data lake. The repository uses 12 data assets beyond the core legal-financial documents: 2 expenditure tables, 1 procurement table, 2 public-works tables, and 4 operational urban datasets, plus 3 official PDFs [1][2][3][4][5][6][7][8][9][10][11][12]. The municipal open data include 119,083 citizen tickets from 2017 to early 2026, 26,467 procurement records from 2012 to 2026, 1,536 historical public works, 49 ongoing works, 7,160 traffic observations, 81 monthly public-transport records, and 175 incident aggregates [6][7][8][9][10][11][12]. These operational layers matter because later optimisation work will only be credible if the fiscal perimeter is first defined correctly [6][7][8][9][10][11][12].

## 2. Data and stylised facts

### 2.1 Source inventory and analytical perimeter

The analysis uses the following evidence base:

| Source | Type | Coverage | Analytical role |
|---|---:|---:|---|
| `Bilancio di Previsione 2025_2027.pdf` | Official budget PDF | 2025–2027 | headline fiscal structure, titles, missions, balance-equilibrium [1] |
| `Piano esecutivo di gestione assestato 2025_2027.pdf` | Official PEG PDF | 2025–2027 | chapter-level appropriations, earmarks, legal vincoli, CDR logic [2] |
| `Rendiconto 2024.pdf` | Official annual account PDF | 2024 | result of administration, SIOPE annexes, commitments/payments/residuals [3] |
| `bilancio-di-previsione-previsione-uscite.csv` | Open-data expenditure | 2013–2025, 2,495 rows | open-data view of budget structure and mission/program aggregation [4] |
| `rendiconto-di-gestione-rendiconto-uscite.csv` | Open-data annual account | 2013–2024, 3,334 rows | computable conversion ratios by mission/title [5] |
| `gare-e-appalti.csv` | Procurement open data | 2012–2026, 26,467 rows | future link between fiscal appropriation and execution pipeline [6] |
| `lavori-pubblici-storico.csv` | Historical works | 1,536 works | capital execution context and territorial project density [7] |
| `lavori-pubblici.csv` | Ongoing works | 49 works | current implementation stock [8] |
| `segnalazioni-open-citizen-relationship-management-czrm.csv` | Citizen tickets | 119,083 tickets | downstream demand pressure layer [9] |
| `traffico-viali.csv` | Traffic | 7,160 observations | downstream mobility pressure layer [10] |
| `tpl_validazioni_km.csv` | Public transport | 81 monthly observations | downstream mobility service layer [11] |
| `incidenti_new.csv` | Incidents | 175 area-year records | downstream safety-risk layer [12] |

### 2.2 Headline fiscal scale versus allocable room

The 2025 total comprehensive expenditure budget is €1.528 billion, falling to €1.384 billion in 2026 and €1.126 billion in 2027 [1]. Within the 2025 total, current expenditure (Titolo 1) is €696.334 million, capital expenditure (Titolo 2) is €472.950 million, expenditure for increases in financial assets (Titolo 3) is €38.800 million, debt repayment (Titolo 4) is €10.801 million, treasury-advance closure (Titolo 5) is €50.000 million, and third-party / giro-account expenditure (Titolo 7) is €259.116 million [1]. In proportional terms, the 2025 expenditure mix is 45.6% current, 31.0% capital, 2.5% financial assets, 0.7% debt service, 3.3% treasury closure, and 17.0% third-party flows [1].

The legally relevant current-resource envelope is narrower than the comprehensive total suggests. In the 2025 equilibrium schedule, Titles 1–3 revenues amount to €706.546 million, against €696.334 million of current expenditure [1]. The current coverage margin is therefore only €10.212 million, equal to 1.45% of Titles 1–3 revenues [1]. Once debt repayment of €10.801 million is included, the margin becomes slightly negative at approximately -€0.588 million [1]. This is a crucial stylised fact: Bologna’s ordinary current envelope is broadly balanced but not wide [1].

### 2.3 Result of administration: large headline, small free core

The 2024 result of administration is €340.737 million [3]. This headline figure is materially misleading if read as freely usable fiscal space. Of the total, €224.066 million are accantonati, €79.609 million are vincolati, and €4.351 million are already destined to investments, leaving only €32.711 million available [3]. The free-surplus ratio is therefore:

$$
FSR = \frac{E}{A} = \frac{32.711}{340.737} \approx 9.6\%
$$

where $E$ is the available component and $A$ is the total result of administration [3]. In other words, 90.4% of the reported result of administration is not freely allocable [3].

The FCDE alone is €176.145 million, equal to 51.7% of the full result of administration and 78.6% of the accantonata component [3]. This single figure already indicates that collection risk and doubtful-credit coverage materially compress discretionary room [3].

### 2.4 Execution and conversion: commitments, payments, FPV, residuals

The open-data annual account allows direct computation of execution metrics on the operating perimeter excluding Missione 60 (treasury advances) and Missione 99 (third-party/giro accounts). On that perimeter, final competence appropriations are €1.911 billion, commitments are €893.795 million, competence payments are €708.364 million, residual payments are €135.080 million, FPV is €286.308 million, and total residual passives carried forward are €201.494 million [5]. This yields four key ratios:

$$
CCR = \frac{I}{CP}
$$

$$
PCR = \frac{PC}{I}
$$

$$
RBR = \frac{EP + EC}{I}
$$

$$
FPV\ intensity = \frac{FPV}{CP}
$$

where $CP$ is competence appropriations, $I$ commitments, $PC$ competence payments, $EP$ prior-year residual passives carried forward, and $EC$ competence-year residual passives [5]. Numerically, the operating-perimeter commitment-conversion ratio is 46.8%, the payment-on-commitment ratio is 79.3%, the residual carry-over ratio is 22.5%, and FPV intensity is 15.0% [5].

### 2.5 Programme priorities and downstream operational relevance

The 2024 open-data annual account identifies the largest programmes by commitments: public transport at roughly €130.3 million, waste management at roughly €100.2 million, childcare and minors at roughly €68.1 million, social exclusion at roughly €56.1 million, and road infrastructure at roughly €48.2 million [5]. At mission level, the largest 2024 commitment aggregates are transport and mobility at roughly €178.9 million, institutional/general management at roughly €178.8 million, social policy/family at roughly €165.8 million, environment at roughly €118.6 million, and education at roughly €105.0 million [5].

The operational datasets show why this matters for later reallocation work. Citizen tickets total 119,083, with the largest first-level categories being urban degradation (24,233), traffic and viability (23,974), environmental degradation (15,644), green maintenance (13,022), and street furniture (9,047) [9]. Historical works total 1,536, heavily concentrated in road-related assets, including 614 paved-road interventions and 234 paved-sidewalk interventions [7]. The procurement file contains 26,467 contracts and large awarded totals in services (€2.038 billion), works (€981.648 million), and supplies (€458.039 million) [6].

## 3. Framework

The analytical framework follows the harmonised local-government accounting structure under D.Lgs. 118/2011 and the equilibrium logic of the TUEL [13][14]. The relevant distinction is not simply between current and capital spending, but among five different states of fiscal reality:

1. **Legal appropriation** — the authorised budget or final competence appropriation ($CP$).  
2. **Activation** — the amount actually transformed into commitments ($I$).  
3. **Cash execution** — the amount actually paid in-year ($PC$ for competence; $PR$ for residuals).  
4. **Deferred but legally committed expenditure** — the residual stock carried over ($EP + EC$).  
5. **Resources already constrained or prudentially unavailable** — FCDE, other accantonamenti, earmarks, and FPV [1][2][3][5][13][14].

A better approximation is:

$$
\text{Allocable room} \approx \text{ordinary flexible revenues} - \text{rigid current expenditure} - \text{debt service} - \text{prudential buffers} - \text{legal earmarks}
$$

### Reproducibility: computation logic

```python
import pandas as pd

bil = pd.read_csv("data/raw/bilancio-di-previsione-previsione-uscite.csv")
ren = pd.read_csv("data/raw/rendiconto-di-gestione-rendiconto-uscite.csv", sep=";")

ren24 = ren[ren["Anno"] == 2024].copy()
oper = ren24[~ren24["Missione"].isin([60, 99])].copy()

CP = oper["Previsioni definitive di competenza"].sum()
I = oper["Impegni"].sum()
PC = oper["Pagamenti in c/competenza"].sum()
FPV = oper["Fondo pluriennale vincolato"].sum()

metrics = {
    "CCR": I / CP,
    "PCR": PC / I,
    "FPV_intensity": FPV / CP,
}
print(metrics)
```

## 4. Scenarios and analysis

### Scenario 1 — Approved-budget central case

Under the approved 2025 budget, the city enters the year with €306.499 million of initial cash and a presumed final cash balance of €296.811 million [1]. Comprehensive expenditure is €1.528 billion, but the decisive short-run operating comparison is between Titles 1–3 revenues (€706.546 million) and current expenditure (€696.334 million) [1]. The resulting current coverage margin is only €10.212 million [1].

### Scenario 2 — Own-source underperformance case

Suppose IMU, IRPEF, and TARI each underperform the 2025 PEG by 3%, while the tourist tax merely repeats its 2024 annual-account level rather than reaching the 2025 PEG target [2][3]. The combined gap is approximately €11.42 million [2][3]. That exceeds the entire 2025 current coverage margin of €10.212 million [1].

### Scenario 3 — Execution-improvement case

Using the 2024 operating-perimeter annual-account data, three levers stand out: improve capex activation, improve payment conversion, and reduce residual carry-over [5]. The policy meaning is straightforward. Bologna’s most valuable “hidden fiscal room” is not found in fictional free surplus. It is found in better commitment sequencing, faster capital activation, more disciplined procurement-to-payment conversion, and lower residual accumulation [2][3][5].

## 5. Risks and caveats

The first caveat is perimeter heterogeneity. The official PDFs and the open-data tables do not always present identical slices of the same accounting universe at the same level of aggregation [1][3][4][5]. The PDFs are the legal reference; the open-data tables are used for computation and decomposition. Where the two differ, the paper privileges the legal-financial meaning of the official PDF and uses the open-data layer for ratio construction and reproducibility [1][3][4][5].

## 6. Comparison and implications

The broader policy lesson is that municipal efficiency should be judged not only by the size of appropriations or by the existence of a positive administration result, but by the relationship among allocability, prudential buffers, conversion discipline, and programme throughput [1][2][3][13][14]. In Bologna’s case, the headline budget is large, but the free core is small and the capital-activation rate is weak [1][3][5]. That points toward reforms in sequencing, procurement governance, PMO capacity, residual reduction, and chapter-level monitoring rather than toward simplistic claims about abundance or scarcity.

## 7. Conclusion

Bologna’s fiscal architecture is best understood as a constrained operating system rather than a large undifferentiated budget. The 2025 expenditure envelope of €1.528 billion coexists with a current-resource cushion of only €10.212 million before debt repayment, a free-surplus component of just €32.711 million within a €340.737 million administration result, and a 2024 operating-perimeter capex commitment rate of only 24.2% [1][3][5]. These are not incidental accounting details: they define the real managerial frontier.

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
