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