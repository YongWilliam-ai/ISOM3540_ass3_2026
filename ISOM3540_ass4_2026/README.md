# ISOM 3540 — Assignment 4 (2026): Question 5

**HKUST · Introduction to Probability Models · Problem Sheet 4**  
**Student ID:** 21089310  
**Assignment deadline:** 16 November 2026 (per supplied problem sheet)  
**Submission:** only the type-written PDF, named `ISOM3540_21089310_ass4.pdf`.

> This folder is a self-contained Assignment 4 collection inside William’s existing `ISOM3540_ass3_2026` repository; it does not modify Assignment 3 calculations.

## Clickable files

| File | Purpose |
|---|---|
| [Submission PDF](ISOM3540_21089310_ass4.pdf) | Two-page complete solution to Question 5(a)–(d), with clickable companion citations |
| [Excel Monte Carlo workbook](ISOM3540_21089310_ass4_MonteCarlo.xlsx) | Inputs, conditional probabilities, 40,000 seeded Monte Carlo replications and native editable convergence chart |
| [Excel plot PNG](ISOM3540_21089310_ass4_Excel_Convergence.png) | Plot embedded in the PDF |
| [LaTeX source](ISOM3540_21089310_ass4.tex) | Full editable mathematical write-up and hyperlinked references |
| [Reproducibility script](reproduce_mc_ass4.py) | Independent NumPy/SciPy simulation, binomial identity and posterior checks |
| [Original computation README](ISOM3540_21089310_ass4_README.txt) | Detailed sample, precision and validation record |
| [Full ZIP bundle](ISOM3540_21089310_ass4_Complete_Package.zip) | All these files bundled, including the revised PDF |

## Assignment model and methodology

The problem specifies \(X\sim\operatorname{Bin}(100,0.5)\) and \(Y\mid X=x\sim\operatorname{Bin}(x,0.3)\). Let \(A=\{12\leq Y\leq18\}\) and \(g(x)=P(A\mid X=x)\). Then

\[
P(A)=E[g(X)]=\sum_{x=0}^{100}\binom{100}{x}2^{-100}g(x).
\]

Simulating \(X\) and averaging \(g(X)\) is a Rao–Blackwellized Monte Carlo estimator, with fixed NumPy generator seed **35402026** and **40,000 samples**.

Independently, binomial thinning yields \(Y\sim\operatorname{Bin}(100,0.15)\), allowing the exact result. Conditional probability in part (d) is computed using the joint distribution; an independent check uses \(X\mid Y=y\stackrel{d}{=}y+\operatorname{Bin}(100-y,7/17)\).

## Verified results

| Quantity | Result |
|---|---:|
| Exact \(P(12\leq Y\leq18)\) | **0.673688405573077** |
| Monte Carlo estimate (40,000 replications) | **0.673295245109373** |
| Monte Carlo standard error | **0.000307681978019** |
| Approximate 95% Monte Carlo CI | **[0.6726921884, 0.6738983018]** |
| Joint \(P(40\leq X\leq60,12\leq Y\leq18)\) | **0.657472496787979** |
| Conditional \(P(40\leq X\leq60\mid12\leq Y\leq18)\) | **0.975929660283668** |

## Reproduce

From this directory:

```sh
python reproduce_mc_ass4.py
pdflatex ISOM3540_21089310_ass4.tex
```

Keep the [chart PNG](ISOM3540_21089310_ass4_Excel_Convergence.png) alongside the `.tex` source. The workbook has 5 sheets: `Parameters`, `Conditional_Lookup`, `MC_Histogram`, `Convergence`, and `Method_and_Audit`.

## Attribution

The original question and constraints are from **HKUST ISOM 3540, Problem Sheet 4 (Fall 2026), instructor Mike So**, Question 5. The wording and numerical parameters are from the user-supplied course assignment. No external market data or empirical datasets are used.

## Document integrity

This folder includes deterministic source materials. For the Excel workbook and chart image, SHA-256 checksums are included below so local copies can be verified.

- `ISOM3540_21089310_ass4_MonteCarlo.xlsx`: `926512b465913c408a74c513b9f9dd2a212842b119476c1bb3510e3b272fc4dc`
- `ISOM3540_21089310_ass4_Excel_Convergence.png`: `949f5d4e1cfb513816436dbceb6b0af2f472f73022e21fbf8252e7d273dd3066`
