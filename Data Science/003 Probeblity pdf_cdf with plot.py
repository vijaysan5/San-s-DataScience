import matplotlib.pyplot as mtpy
import numpy as num
from scipy.stats import norm, binom

# PDF > Probability Density Function
mean_val = 85
standard_d = 10
line = num.linspace(50, 120, 512)
pdf = norm.pdf(line, mean_val, standard_d)
mtpy.figure(figsize=(8,6))
mtpy.plot(line, pdf)
mtpy.title("PDF > Normal Distribution")
mtpy.xlabel("Line")
mtpy.ylabel("PDF value")
mtpy.show()


# CDF > Cumulative Distribution Function
cdf = norm.cdf(line, mean_val, standard_d)
mtpy.figure(figsize=(8,6))
mtpy.plot(line, cdf)
mtpy.title("CDF > cumulative Distribution")
mtpy.xlabel("Line")
mtpy.ylabel("CDF value")
mtpy.show()



mean_val =115
standard_d = 10
line = num.linspace(80, 150, 499)
pdf = norm.pdf(line, mean_val, standard_d)
mtpy.figure(figsize=(8,6))
mtpy.plot(line, pdf)
mtpy.title("PDF > Normal Dist ___ grid > True")
mtpy.xlabel("line sp")
mtpy.ylabel("pdf value g")
mtpy.grid(True)
mtpy.show()


# CDF > Cumulative Distribution Function
cdf = norm.cdf(line, mean_val, standard_d)

mtpy.figure(figsize=(8,6))
mtpy.plot(line, cdf)
mtpy.title("CDF > cumulative Dist ___ grid > True")
mtpy.xlabel("line sp")
mtpy.ylabel("cdf value g")
mtpy.grid(True)
mtpy.show()



# BINOMIAL DISTRIBUTION :
x = 15
y = 0.5

ax = num.arange(0, x + 1)

binomial_pmf = binom.pmf(ax, x, y)
print("Binomial PMF value :", binomial_pmf)
mtpy.figure(figsize=(9,6))
mtpy.bar(ax, binomial_pmf)
mtpy.xlabel("Rangae")
mtpy.ylabel("PMF value")
mtpy.title("Binomial - PMF")
mtpy.grid()
mtpy.show()

binomial_cdf = binom.cdf(ax, x, y)
print("Binomial CDF value :", binomial_cdf)
mtpy.figure(figsize=(9,6))
mtpy.plot(ax, binomial_cdf, marker="o")
mtpy.xlabel("Rangae")
mtpy.ylabel("CDF value")
mtpy.title("Binomial - CDF")
mtpy.grid()
mtpy.show()



# Binomial (pmf = 5) (cdf = 7)
exact_5_pmf = binom.pmf(5, x, y)
print("PMF 5 :", exact_5_pmf)
lessthan_7_cdf = binom.cdf(7, x, y)
print("CDF 7 :", lessthan_7_cdf)


# Binomial (pmf = 6) (cdf = 8)
exact_6_pmf = binom.pmf(6, x, y)
print("PMF 6 :", exact_6_pmf)
lessthan_8_cdf = binom.cdf(8, x, y)
print("CDF 8 :", lessthan_8_cdf)
