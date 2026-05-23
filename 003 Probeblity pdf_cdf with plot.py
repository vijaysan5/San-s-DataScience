import matplotlib.pyplot as mtpy
import numpy as num
from scipy.stats import norm

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



mean_val = 81
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