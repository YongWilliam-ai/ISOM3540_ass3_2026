ISOM3540 — Assignment 3, Question 5 — Student ID 21089310

DELIVERABLES
- ISOM3540_21089310_ass3.pdf : the four-page, typed Q5 submission.
- ISOM3540_21089310_ass3.tex : editable LaTeX source.
- figure_1_ewma_variance.png : plotted EWMA variance.
- figure_2_var_5pct.png : realized returns vs 5% VaR thresholds.
- figure_3_var_1pct.png : realized returns vs 1% VaR thresholds.
- ISOM3540_21089310_ass3_Excel.xlsx : Excel calculations and 3 Excel-native charts.
- analysis.csv : all 1,255 daily results, 2021-2025.
- all_closes.csv : S&P 500 daily closing-price inputs, including 2020 initialization.

REPRODUCE
Install a LaTeX distribution such as TeX Live or use Overleaf. Put the .tex and
three PNG figures in the same directory, then compile the .tex file with pdfLaTeX.
The Excel file includes the input prices, formulas, Kupiec statistics and charts.

ASSUMPTIONS
RiskMetrics EWMA lambda = 0.94; standardized Student t degrees of freedom = 5;
initial one-day EWMA variance = average squared percentage-point return over
60 preceding trading sessions from 7 October through 31 December 2020;
zero conditional mean. Dates, return units and price sources are in the PDF.

SOURCES
S&P 500 on FRED: https://fred.stlouisfed.org/series/SP500
FRED daily table: https://fred.stlouisfed.org/data/SP500
Historical FRED price mirror:
https://github.com/AguilarMike/marketobservatory/blob/main/data/sp500.csv

FINAL VALIDATION
Number of 2021-2025 observations: 1255.
Normal 5% and 1% breaches: 74, 26.
Standardized-t 5% and 1% breaches: 81, 19.
Normal 5% and 1% Kupiec coverage p-values: .1559922, .00085325.
Standardized-t 5% and 1% Kupiec coverage p-values: .0234094, .0889741.


GITHUB REPOSITORY AND CLICKABLE REFERENCES
Repository: https://github.com/YongWilliam-ai/ISOM3540_ass3_2026
Source notes: https://github.com/YongWilliam-ai/ISOM3540_ass3_2026/blob/main/README_SOURCES.txt
Submission PDF includes clickable FRED links and a repository reference.

REPOSITORY PUBLICATION CAVEAT
A local, complete source ZIP and Excel workbook accompany the submission.
The existence of these local artifacts does not by itself confirm a GitHub upload.
Only files visible on GitHub's main branch can be treated as publicly published.
