
import numpy as np
from scipy import stats

x_bar = 4
s = 1.5
n = 20
confidence = 0.90

df = n - 1

t_critical = stats.t.ppf((1 + confidence) / 2, df)

margin_of_error = t_critical * (s / np.sqrt(n))

lower_bound = x_bar - margin_of_error
upper_bound = x_bar + margin_of_error

print(f"t-critical value: {t_critical:.3f}")
print(f"Confidence Interval (90%): ({lower_bound:.2f}, {upper_bound:.2f})")



import numpy as num
import pandas as pan
import matplotlib.pyplot as mtpy
from scipy import stats
from scipy.stats import t

values = num.array([12, 23, 34, 45, 56, 67, 78, 89, 90, 98])
Mean_val = num.mean(values)
pop_mean = 56

t_stat, p_val = t.ttest_1samp(values, pop_mean)

print("Mean Value :", Mean_val, "\nStatistic :", t_stat, "\nP_Value :", p_val)

if p_val < 0.5 :
    print("Reject")
else:
    print("Accept")






import pandas as pan
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

dtf = pan.read_csv("San's  DataScience Folder\\ds csv files\\student dataset_new.csv")
print("CSV Info :\n", dtf.info())

print("Null :\n", dtf.isna().sum())
print("Duplicate :\n", dtf.duplicated().sum())
dtcopy = dtf.drop("ethnic.group", axis=1)
print("after droped 'ethnic.group' column :\n", dtcopy.info())
data = dtf
# stri = data.select_dtypes(include="str").columns
flt = data.select_dtypes(include="float64").columns
lben = LabelEncoder()
for y in flt:
    data[y] = lben.fit_transform(data[y])
print(data.info())

string = data.select_dtypes(include="str").columns
for z in string :
    data[z] = lben.fit_transform(data[z])
print(data.info())

df = pan.DataFrame(data, columns=dtcopy.columns)
print("\nDataframe---------:\n", df)

stsclr = StandardScaler()
st = stsclr.fit_transform(df.drop("age", axis=1))
yz = df["age"]

sttr, stts, yztr, yzts = train_test_split(st, yz, test_size=0.2)
print("\nTrain Value :\n", sttr)