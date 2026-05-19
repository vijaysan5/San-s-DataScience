import pandas as pan
import matplotlib.pyplot as mtpy
import numpy as num

# Normal Distribution = 0 
# Skew Value = 0.1 to 0.5

Data = pan.read_csv("San's  Python Folder\San csv files\zip files\\household-living-costs-price-indexes-march-2026-quarter-group-facts.csv")
print(Data.info())

file_Copy = Data.copy()

dfile = Data.select_dtypes(include="int64")

for i in dfile:
    print("Skew :", i, dfile[i].skew())
    print("Kurt : ", i, dfile[i].kurt())



# YEAR >>> FIXED SKEW PLOT
file_Copy['year'] = num.log1p(Data['year'])
print("Fixed Skew > year", file_Copy['year'].skew())
x = file_Copy['year']
mtpy.plot(x, label="wave", color='red', linestyle='-', linewidth=1)
mtpy.xlabel("X Row")
mtpy.ylabel("Y Row")
mtpy.title("YEAR >>> FIXED SKEW PLOT")
mtpy.legend()
mtpy.grid()
mtpy.show()

# TOT_HHS >>> FIXED SKEW PLOT
file_Copy['tot_hhs'] = num.log1p(Data['tot_hhs'])
print("Fixed Skew > tot_hhs", file_Copy['tot_hhs'].skew())
x = file_Copy['tot_hhs']
mtpy.plot(x, label="wave", color='red', linestyle='-', linewidth=1)
mtpy.xlabel("X Row")
mtpy.ylabel("Y Row")
mtpy.title("TOT_HHS >>> FIXED SKEW PLOT")
mtpy.legend()
mtpy.grid()
mtpy.show()

# OWN >>> FIXED SKEW PLOT
file_Copy['own'] = num.log1p(Data['own'])
print("Fixed Skew > own", file_Copy['own'].skew())
x = file_Copy['own']
mtpy.plot(x, label="wave", color='red', linestyle='-', linewidth=1)
mtpy.xlabel("X Row")
mtpy.ylabel("Y Row")
mtpy.title("OWN >>> FIXED SKEW PLOT")
mtpy.legend()
mtpy.grid()
mtpy.show()

# OWN_WM >>> FIXED SKEW PLOT
file_Copy['own_wm'] = num.log1p(Data['own_wm'])
print("Fixed Skew > own_wm", file_Copy['own_wm'].skew())
x = file_Copy['own_wm']
mtpy.plot(x, label="wave", color='red', linestyle='-', linewidth=1)
mtpy.xlabel("X Row")
mtpy.ylabel("Y Row")
mtpy.title("OWN_WM >>> FIXED SKEW PLOT")
mtpy.legend()
mtpy.grid()
mtpy.show()

# INCOME >>> FIXED SKEW PLOT
file_Copy['income'] = num.log1p(Data['income'])
print("Fixed Skew > income", file_Copy['income'].skew())
x = file_Copy['income']
mtpy.plot(x, label="wave", color='red', linestyle='-', linewidth=1)
mtpy.xlabel("X Row")
mtpy.ylabel("Y Row")
mtpy.title("INCOME >>> FIXED SKEW PLOT")
mtpy.legend()
mtpy.grid()
mtpy.show()

# EXPENDITURE >>> FIXED SKEW PLOT
file_Copy['expenditure'] = num.log1p(Data['expenditure'])
print("Fixed Skew > expenditure", file_Copy['expenditure'].skew())
x = file_Copy['expenditure']
mtpy.plot(x, label="wave", color='red', linestyle='-', linewidth=1)
mtpy.xlabel("X Row")
mtpy.ylabel("Y Row")
mtpy.title("EXPENDITURE >>> FIXED SKEW PLOT")
mtpy.legend()
mtpy.grid()
mtpy.show()

# EQV_INCOME >>> FIXED SKEW PLOT
file_Copy['eqv_income'] = num.log1p(Data['eqv_income'])
print("Fixed Skew > eqv_income", file_Copy['eqv_income'].skew())
x = file_Copy['eqv_income']
mtpy.plot(x, label="wave", color='red', linestyle='', linewidth=1)
mtpy.xlabel("X Row")
mtpy.ylabel("Y Row")
mtpy.title("EQV_INCOME >>> FIXED SKEW PLOT")
mtpy.legend()
mtpy.grid()
mtpy.show()

# EQV_EXP >>> FIXED SKEW PLOT
file_Copy['eqv_exp'] = num.log1p(Data['eqv_exp'])
print("Fixed Skew > eqv_exp", file_Copy['eqv_exp'].skew())
x = file_Copy['eqv_exp']
mtpy.plot(x, label="wave", color='red', linestyle='-', linewidth=1)
mtpy.xlabel("X Row")
mtpy.ylabel("Y Row")
mtpy.title("EQV_EXP >>> FIXED SKEW PLOT")
mtpy.legend()
mtpy.grid()
mtpy.show()


"________ONE >>> FIX Skew Value"
import pandas as pan
import numpy as num
New_data = pan.read_csv("San's  DataScience Folder/ds csv files\\overseas-trade-indexes-december-2025-quarter-provisional.csv")
print(New_data.info())
Copy_New = New_data.copy()
skfile = New_data.select_dtypes(include='int64')

for x in skfile:
    print("Skew Value :", x, skfile[x].skew())
    print("Kurt Value :", x, skfile[x].kurt())
#  Fixing Skew Value
Copy_New['MAGNTUDE'] = num.log1p(New_data['MAGNTUDE'])
print("Fixed Skew > MAGNTUDE", Copy_New['MAGNTUDE'].skew())


"________TWO >>> FIX Skew Value"
import pandas as pan
rental = pan.read_csv("San's  DataScience Folder\ds csv files\\rental-price-indexes-september-2023.csv")
print(rental.info())
c_rent = rental.copy()
skrent = rental.select_dtypes(include='int64')

for y in skrent:
    print("Skew Value :", y, skrent[y].skew())
    print("Kurt Value :", y, skrent[y].kurt())


"________THREE >>> FIX Skew Value"
import pandas as pan
import numpy as num
unique = pan.read_csv("San's  DataScience Folder\ds csv files\\unique-passenger-counts-over-100-by-NZ-port-and-citizenship-year-ended-june-2020.csv")
print(unique.info())
c_uniq = unique.copy()
skuniq = unique.select_dtypes(include='int64')

for a in skuniq:
    print("Skew Value :", a, skuniq[a].skew())
    print("Kurt Value :", a, skuniq[a].kurt())
# Fixing Skew Value (Count)
c_uniq['Count'] = num.log1p(unique['Count'])
print("Fixing Count Value's Skew :", c_uniq['Count'].skew())

"________FOUR >>> FIX Skew Value"
import pandas as pan
health = pan.read_csv("San's  DataScience Folder\ds csv files\\National-labour-force-projections-2020base-2073.csv.csv")
print(health.info())
c_health = health.copy()
skheal = health.select_dtypes(include='int64')

for n in skheal:
    print("Skew Value :", n, skheal[n].skew())          # Normal Distribution
    print("Kurt Value :", n, skheal[n].kurt())

"_______FIVE >>> Cheack Skew"
import pandas as pan
zillow = pan.read_csv("San's  DataScience Folder\ds csv files\\zillow.csv")
print(zillow.info())
c_zil = zillow.copy()
skzill = zillow.select_dtypes(include='int64')

for m in skzill:
    print("Zill Skew :", m, skzill[m].skew()) 
    print("Zill Kurt :", m, skzill[m].kurt())

"""
Zill Skew : Index 0.0                                       # Normal Dist
Zill Skew :  "Living Space (sq ft)" 0.3258440245799792      # Skew
Zill Skew :  "Beds" 0.32825918059584397                     # Skew
Zill Skew :  "Zip" -1.1764847963583702                      
Zill Skew :  "Year" -0.9438837076096187
Zill Skew :  "List Price ($)" 0.46385727085443346           # Skew
"""