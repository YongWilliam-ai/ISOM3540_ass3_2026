# Source and verification references

**Primary educational source:** Mike So, ISOM 3540 Introduction to Probability Models, Problem Sheet 4 (Fall 2026), Question 5, supplied by the student (not redistributed). It defines the nested binomial model and requires parts (a)–(d).

**Methods used:** finite sum for conditional binomial probability; law of total expectation; Rao–Blackwellized Monte Carlo estimation; binomial thinning; Bayes' theorem; and a three-category multinomial argument for the conditional law of interested non-buyers given the observed buyer count.

**Workbook:** [ISOM3540_21089310_ass4_MonteCarlo.xlsx](ISOM3540_21089310_ass4_MonteCarlo.xlsx), seed 35402026, 40,000 independent binomial X draws, 40 batches of 1,000, five worksheets, native Excel editable line chart. The [PNG](ISOM3540_21089310_ass4_Excel_Convergence.png) is an export used in the [PDF](ISOM3540_21089310_ass4.pdf).

**Independent calculation:** [reproduce_mc_ass4.py](reproduce_mc_ass4.py) calculates both exact distributions and the seeded Monte Carlo estimate, and verifies the posterior probability by a second route.

**No external empirical observations:** this is a fully specified textbook probability problem, so there are no fetched data sources to cite.
