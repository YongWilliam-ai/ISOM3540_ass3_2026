"""ISOM3540 HW4 Q5: reproducible Monte Carlo + two exact cross-checks.

Uses NumPy and SciPy; independent of the Excel workbook. Run:
    python reproduce_mc_ass4.py
"""
import numpy as np
from scipy.stats import binom

n, p1, p2 = 100, 0.5, 0.3
x = np.arange(n + 1)
g = binom.cdf(18, x, p2) - binom.cdf(11, x, p2)

# Method 1: marginal Y ~ Bin(100, 0.15)
exact = binom.cdf(18, n, p1 * p2) - binom.cdf(11, n, p1 * p2)
# Method 2: exact total expectation over X
by_x = binom.pmf(x, n, p1)
total_expectation = np.dot(by_x, g)
assert np.isclose(exact, total_expectation, atol=1e-13)

# Part (b): fixed-seed Rao-Blackwellized Monte Carlo (X only)
M, seed = 40_000, 35402026
rng = np.random.default_rng(seed)
x_draws = rng.binomial(n, p1, size=M)
values = g[x_draws]
mc = values.mean()
se = values.std(ddof=1) / np.sqrt(M)

# Part (d): direct joint event numerator / denominator
numerator = np.sum(by_x[40:61] * g[40:61])
posterior = numerator / exact
# Independent posterior check: X|Y=y = y + Bin(100-y, 7/17)
q = p1 * (1 - p2) / (1 - p1 * p2)
alt = sum(
    binom.pmf(y, n, p1 * p2) *
    (binom.cdf(60-y, n-y, q) - binom.cdf(39-y, n-y, q))
    for y in range(12, 19)
) / exact
assert np.isclose(posterior, alt, atol=1e-13)

print(f"Exact binomial:       {exact:.15f}")
print(f"Exact E[g(X)]:        {total_expectation:.15f}")
print(f"Monte Carlo estimate: {mc:.15f}")
print(f"Monte Carlo SE:       {se:.15f}")
print(f"Monte Carlo 95% CI:  [{mc-1.96*se:.12f}, {mc+1.96*se:.12f}]")
print(f"Joint event numerator:{numerator:.15f}")
print(f"Posterior:            {posterior:.15f}")
print(f"Posterior check:      {alt:.15f}")
