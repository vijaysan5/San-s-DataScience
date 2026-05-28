import pandas as pan
from scipy.stats import zscore
import matplotlib.pyplot as mtpy

hhold = pan.read_csv("San's  DataScience Folder/ds csv files/household-living-costs-price-indexes-march-2026-quarter-group-facts.csv")
print(hhold.info())

# "One ___"
# print("\nIncome's Zscore :\n", zscore(hhold["income"]))
# "Two ___"
# Own = hhold["own"]
# print("\nOwn's Zscore :\n", zscore(Own))


Int = hhold.select_dtypes(include="int64")
for x in Int :
    print("\nint64 > Zscore Value :\n", zscore(Int[x]))

Float = hhold.select_dtypes(include="float64")
for y in Float:
    print("\nfloat64 > Zscore Value :\n", zscore(Float[y]))



# import pandas as pan
# from scipy.stats import zscore
Zill = pan.read_csv("San's  DataScience Folder\\ds csv files\\zillow.csv")
print(Zill.info())

for z in Zill:
    print("\nZill Dataset's Overall Zscore Value :\n", zscore(Zill[z]))


plot = zscore(hhold["tot_hhs"])
mtpy.hist(plot, bins=10, color="r", edgecolor="black")
mtpy.show()

plot = zscore(hhold["age"])
age = hhold["age"]
mtpy.bar(plot, age, edgecolor="black")
mtpy.show()




"""__________~ T Distribution ~__________"""

import pandas as pan
import numpy as num
from scipy.stats import t, ttest_1samp
import matplotlib.pyplot as mtpy

# df = n - 1   >>> Formula

df = 12
x = num.linspace(-5, 5, 532)
tdist = t.pdf(x, df)
mtpy.plot(x, tdist)
mtpy.title("T Distribution Plot")
mtpy.xlabel("Random linespace")
mtpy.ylabel("T-dist pdf")
mtpy.show()



values = num.array([12, 23, 34, 45, 56, 67, 78, 89, 90, 98, 87, 65, 54, 21])
Mean_val = num.mean(values)
pop_mean = 78

t_stat, p_val = ttest_1samp(values, pop_mean)

print("Mean Value :", Mean_val, "\nStatistic :", t_stat, "\nP_Value :", p_val)

if p_val < 0.5 :
    print("Reject")
else:
    print("Accept")

