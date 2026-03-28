# Procurement Efficiency, Capex Absorption, and Intervention Performance
## Bologna’s mobility-maintenance pipeline under fiscal, legal, and territorial constraints

## Abstract

This note examines Bologna’s procurement system, capital-absorption dynamics, and intervention-performance profile by integrating 12 municipal sources: the 2025–2027 budget, the 2025–2027 PEG, the 2024 annual account, open-data budget and annual-account tables, procurement records, historical and current public-works registries, citizen tickets, traffic counts, public-transport validations, and incident statistics.[1][2][3][4][5][6][7][8][9][10][11][12] The analytical objective is not to describe procurement in isolation, but to assess whether Bologna’s legally authorised spending is converted into works, payments, and spatially rational intervention patterns.

Three findings dominate. First, the procurement universe is large but structurally dual. The procurement file contains 26,467 procedures between 2012 and 2026, with €4.672 billion of base tender value, €3.478 billion of awarded value, and €2.310 billion of liquidated amounts.[6] Direct-award procedures account for 21,578 records, or 81.5% of all procedures, but only 49.2% of awarded value; by contrast, open procedures account for 609 records, or 2.3% of all procedures, but 40.1% of awarded value.[6] The system is therefore simultaneously fragmented in procedural count and concentrated in economic value.[6]

Second, Bologna’s mobility-and-maintenance perimeter is economically large but execution-constrained. A broad keyword-defined mobility-maintenance subset of the procurement file contains 2,453 procedures, €1.531 billion of tender value, €1.215 billion of awarded value, and €723.6 million of liquidations.[6] In the legal budget, Mission 10 totals €326.258 million in 2025, while Programme 1005 `Viabilità e infrastrutture stradali` totals €33.292 million and Programme 1002 `Trasporto pubblico locale` totals €292.563 million.[1] In the 2024 annual account, Programme 1005 shows €48.194 million of commitments and €37.044 million of competence payments, while Programme 1002 shows €130.325 million of commitments and €99.766 million of competence payments.[3] Yet the capital-activation problem remains severe: within 2024 Title 2 expenditure, the commitment-conversion ratio is only 35.5% for Programme 1005 and 23.4% for Programme 1002.[5]

Third, intervention supply is materially road-heavy but not perfectly aligned with territorial pressure. The historical works file contains 1,536 interventions, of which 1,243, or 80.9%, are in roads, sidewalks, bridges, roadbeds, and cycle paths.[7] The current works file contains 49 ongoing interventions, of which 48, or 98.0%, are in the same road-space perimeter and 23, or 46.9%, are explicitly tram-related.[8]

## 1. Introduction

A municipality can have a large procurement perimeter and still underperform operationally if three conversion steps remain weak: appropriation into commitment, commitment into payment, and payment into territorially effective intervention. Bologna is a particularly strong case because the city combines a large mobility and maintenance perimeter with a dense historic urban form, heavy corridor concentration, and a broad open-data stack that permits joint analysis of budgets, contracts, works, complaints, traffic, incidents, and public-transport demand.[1][2][3][4][5][6][7][8][9][10][11][12]

## 2. Data and stylised facts

### 2.1 Procurement universe: fragmented count, concentrated value

The procurement file contains 26,467 procedures between 2012 and 2026.[6] Total base tender value amounts to €4.672 billion, awarded value to €3.478 billion, and liquidated amounts to €2.310 billion.[6] The aggregate award-to-base ratio is therefore 74.4%, while the cumulative liquidation-to-award ratio is 66.4%.[6]

By appalto type, services dominate both count and awarded value: 15,617 service procedures account for €2.038 billion awarded and €1.414 billion liquidated.[6] Works account for 849 procedures, €981.648 million awarded, and €733.046 million liquidated.[6] Supplies account for 7,633 procedures, €458.039 million awarded, and €103.102 million liquidated.[6]

### 2.2 Mobility and maintenance procurement subset

A broad keyword-defined mobility-maintenance perimeter built on roads, viability, signage, sidewalks, bridges, cycle paths, tram, TPL, lighting, asphalt, road-surface and related terms identifies 2,453 procedures, or 9.3% of the full procurement stock.[6] That subset contains €1.531 billion of base tender value, €1.215 billion of awarded value, and €723.639 million of liquidations.[6] In awarded-value terms, the subset alone accounts for 34.9% of the full procurement universe.[6]

### 2.3 Legal budget and annual-account execution

In the 2025 budget PDF, Mission 10 `Trasporti e diritto alla mobilità` totals €326.258 million, with Programme 1002 `Trasporto pubblico locale` at €292.563 million and Programme 1005 `Viabilità e infrastrutture stradali` at €33.292 million.[1]

In the 2024 legal annual account, Programme 1002 shows €547.075 million of definitive competence appropriations, €130.325 million of commitments, €99.766 million of competence payments, and €73.799 million of FPV.[3] Programme 1005 shows €97.518 million of definitive competence appropriations, €48.194 million of commitments, €37.044 million of competence payments, and €27.006 million of FPV.[3]

### 2.4 Chapter-level evidence from the PEG

The PEG provides operational granularity. Within Programme 1005, chapter `U33500-000` `MANUTENZIONE DELLA VIABILITA': PRESTAZIONI DI SERVIZI` carries €2.632 million in 2025, €2.620 million in 2026, and €2.620 million in 2027.[2] Chapter `U33460-000` `MANUTENZIONE DELLA VIABILITA' E DELLA SEGNALETICA STRADALE - CONTRO AVANZO DI AMMINISTRAZIONE` shows €119,840 in 2025.[2]

## 3. Framework

The relevant analytical object is not a single ratio, but a conversion chain:

$$
\text{Appropriation} \rightarrow \text{Tender} \rightarrow \text{Award} \rightarrow \text{Commitment} \rightarrow \text{Payment} \rightarrow \text{Physical intervention} \rightarrow \text{Pressure relief}
$$

The paper uses five core indicators: tender depth ratio, liquidation realisation ratio, capex commitment-conversion ratio, FPV deferral ratio, and a territorial saturation ratio.[5][6][8][9]

### Reproducibility: Python skeleton

```python
import pandas as pd

ga = pd.read_csv("data/raw/gare-e-appalti.csv", sep=";", low_memory=False)
ren = pd.read_csv("data/raw/rendiconto-di-gestione-rendiconto-uscite.csv", sep=";")

for c in [
    "Importo appalto (Euro)",
    "Importo di aggiudicazione (Euro)",
    "Importo delle somme liquidate (Euro)",
]:
    ga[c] = pd.to_numeric(ga[c], errors="coerce")

base = ga["Importo appalto (Euro)"].sum()
award = ga["Importo di aggiudicazione (Euro)"].sum()
liq = ga["Importo delle somme liquidate (Euro)"].sum()

tdr = award / base
lrr = liq / award
print({"tdr": tdr, "lrr": lrr})
```

## 4. Scenarios and analysis

### Scenario 1 — Status quo

Under the status quo, Bologna’s procurement system remains count-fragmented and value-concentrated. Full-stock direct awards account for 81.5% of procedures but 49.2% of awarded value, while open procedures account for 2.3% of procedures but 40.1% of awarded value.[6]

### Scenario 2 — Bundling repetitive maintenance

If 20% of direct-award procedures were consolidated into larger framework or lot-based structures, Bologna would convert 355 direct-award procedures into a smaller administrative stock.[6] If those 355 procedures were regrouped into 40 lots, the net reduction would be 315 procedures.[6]

### Scenario 3 — Capex activation improvement

With €72.682 million of Programme 1005 Title-2 competence appropriations and a current conversion ratio of 35.5%, raising that ratio to 45.0% would generate approximately €6.89 million of additional activated capital.[5] The analogous calculation for Programme 1002 is roughly €34.0 million if the activation ratio rises from 23.4% to 30.0%.[5]

## 5. Risks and caveats

The first caveat is data-perimeter heterogeneity. The legal budget PDF, the open-data budget table, the legal annual account, and the open-data annual-account table are not always numerically identical at every level of aggregation.[1][3][4][5]

## 6. Comparison and implications

The city’s next-best lever is not indiscriminate spending compression. It is better throughput: fewer low-value administrative repetitions, stronger capex activation, and more pressure-aware sequencing.[1][2][3][5][6]

## 7. Conclusion

Bologna’s mobility-and-maintenance problem is not one of nominal scale. It is one of conversion quality. The city has a very large procurement universe with €3.478 billion of awarded value across the long series, a large mobility-maintenance subset with €1.215 billion of awarded value, and a major legal budget perimeter in Mission 10.[1][6]

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
