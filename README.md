# ISOM 3540 — Assignment 3, Question 5 (Fall 2026)

**HKUST · Introduction to Probability**  
**Student ID:** 21089310  
**Assignment due:** 30 October 2026

This repository documents the data sources, analysis conventions, and reproducibility materials for Question 5, an S&P 500 daily RiskMetrics and Value-at-Risk study covering **2021–2025**.

## Analysis at a glance

The study uses **1,255 daily returns**, calculated from consecutive trading-day closing prices (not calendar-day interpolation):

\[
R_t=100\frac{P_t-P_{t-1}}{P_{t-1}},\qquad
\sigma_t^2=\lambda\sigma_{t-1}^2+(1-\lambda)R_{t-1}^2.
\]

The numerical illustration fixes \(\lambda=0.94\), an initial variance from the final 60 sessions of 2020, a zero conditional mean, and standardized Student’s \(t\) degrees of freedom \(\nu=5\). These are **explicit modeling choices**, not values supplied by the assignment.

| Risk model | Tail probability | Exceptions (out of 1,255) | Kupiec unconditional-coverage p-value |
|---|---:|---:|---:|
| Normal RiskMetrics | 5% | 74 | 0.1559922 |
| Normal RiskMetrics | 1% | 26 | 0.00085325 |
| Standardized-\(t_5\) RiskMetrics | 5% | 81 | 0.0234094 |
| Standardized-\(t_5\) RiskMetrics | 1% | 19 | 0.0889741 |

The normal model is better calibrated at the 5% tail and the standardized-\(t\) model at the 1% tail **under these assumptions**. Passing a coverage-frequency test does not establish independence of tail exceptions.

## Companion-file guide

The reproducibility bundle was prepared with these names:

| File | What it contains |
|---|---|
| `ISOM3540_21089310_ass3.pdf` | Typed Question 5 submission with three figures |
| [ISOM3540_21089310_ass3.tex](ISOM3540_21089310_ass3.tex) | Editable LaTeX source (published) |
| `ISOM3540_21089310_ass3_Excel.xlsx` | Excel inputs, formulas, test statistics, and three editable charts |
| [analysis.csv](analysis.csv) | Complete daily 2021–2025 returns, volatility and VaR series (published) |
| [all_closes.csv](all_closes.csv) | Closing prices including the 2020 initialization period (published) |
| `figure_1_ewma_variance.png` | Time series of RiskMetrics variance |
| `figure_2_var_5pct.png` | Realized returns against 5% VaR thresholds |
| `figure_3_var_1pct.png` | Realized returns against 1% VaR thresholds |
| `ISOM3540_21089310_ass3_Source_Bundle.zip` | Complete reproducibility archive |
| [`README_SOURCES.txt`](README_SOURCES.txt) | Source citations and verification notes |

**Repository publication status:** Verified on the main branch: this README, [source notes](README_SOURCES.txt), [LaTeX source](ISOM3540_21089310_ass3.tex), [daily VaR calculations](analysis.csv), [daily closing prices](all_closes.csv), and [backtest summary](backtest_summary.csv). **Pending separate binary upload:** the PDF, Excel workbook, PNG figures and complete ZIP; the listed names are not claims that these binary files have been published. They are included in the downloadable ChatGPT source bundle.

## Data provenance

1. **Primary:** [S&P Dow Jones Indices LLC, S&P 500 (SP500) — FRED](https://fred.stlouisfed.org/series/SP500).
2. **Daily source table:** [FRED SP500 historical data](https://fred.stlouisfed.org/data/SP500).
3. **Historical price mirror:** [AguilarMike/marketobservatory — data/sp500.csv](https://github.com/AguilarMike/marketobservatory/blob/main/data/sp500.csv), used as documented in the assignment PDF.

S&P 500 series represents the **price index**, not a total-return index. Daily return computations skip market holidays and use the previous observed trading-day close.

## PDF and Excel instructions

- The **submission PDF** is the required item for the course, not the reproducibility ZIP or Excel.
- If compiling from LaTeX, keep the three `figure_*.png` files alongside `ISOM3540_21089310_ass3.tex` and compile with `pdflatex`.
- Review the `Assumptions`, `Warmup_2020`, `Daily_Data`, `Backtest`, and `Excel_Charts` worksheets in the companion workbook.

For exact coefficients, model definitions, and interpretation, consult the submission PDF and [README_SOURCES.txt](README_SOURCES.txt).
