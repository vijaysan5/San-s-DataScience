import numpy as num
import pandas as pan
import matplotlib.pyplot as mtpy
import seaborn as sb
from scipy.stats import norm

house = pan.read_csv("San's  DataScience Folder/ds csv files/household-living-costs-price-indexes-march-2026-quarter-group-facts.csv")
# print("Read house ob :", house)

mean = num.mean(house.income)
stand = num.std(house.income)
count = house.income.count()
print(count)
data = num.random.normal(mean, stand, count)
mtpy.hist(data, bins=10, density= True, alpha= 0.5, edgecolor= "#000000")
dfmin,dfmax = mtpy.xlim()
line = num.linspace(dfmin, dfmax, count)
plot = norm.pdf(line, mean, stand)
mtpy.plot(line, plot, 'r')
mtpy.show()
print("Mean  :", mean)
print("Stand :", stand)
print("Count :", count)


newfit = house["expenditure"]
abc, xyz = norm.fit(newfit)
mtpy.hist(newfit, bins=10, density= True, alpha=0.5, color="red", edgecolor="#000000")
ddmin, ddmax = mtpy.xlim()
line_ = num.linspace(ddmin, ddmax, 100)
plot_ = norm.pdf(line_, abc, xyz)
mtpy.plot(line, plot, "b")
mtpy.show()
print("Mean  :", abc)
print("Stand :", xyz)

"Z score base___"
from scipy.stats import zscore
# newfit = house["expenditure"]
print("\n\nZscore Values:\n", zscore(newfit))


from scipy import stats
newhouse = house["eqv_income"]
nhmean = num.mean(newhouse)
nhstd_er = stats.sem(newhouse)
con_int = 0.98
Interval = stats.norm.interval(con_int, loc=nhmean, scale=nhstd_er)

mtpy.hist(newhouse, bins=10, color="#4FE5EB", alpha=0.7, edgecolor="#0285ff")
mtpy.axvline(nhmean, color="red", linewidth=2, label="nhmean")
mtpy.axvline(Interval[0], color="blue", linestyle=":")
mtpy.axvline(Interval[1], color="green", linestyle=":")
mtpy.show()

house.plot()
mtpy.show()