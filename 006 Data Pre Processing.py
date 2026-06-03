import pandas as pan
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split


# import pandas as pan
# data = pan.read_csv("San's  DataScience Folder\\ds csv files\\student dataset_new.csv")
# print("CSV Info :\n", data.info())

# print("Null :\n", data.isna().sum())
# print("Duplicate :\n", data.duplicated().sum())
# dtcopy = data.drop("ethnic.group", axis=1)
# print("after droped 'ethnic.group' column :\n", dtcopy.info())



dataset = pan.read_csv("San's  DataScience Folder\\ds csv files\\effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv")
print("CSV Info :\n", dataset.info())

print("Null :\n", dataset.isna().sum())
print("Duplicate :\n", dataset.duplicated().sum())

# Change >>> Object to int64
obj_int = dataset.select_dtypes(include="object").columns
lben = LabelEncoder()
for x in obj_int:
    dataset[x] = lben.fit_transform(dataset[x])
print(dataset.info())

# Standards Scaler convert
stsclr = StandardScaler()
dtss = stsclr.fit_transform(dataset)
print("\nStandard Scaler --------:\n", dtss)

# Convert to Data Frame 
dtfrm = pan.DataFrame(dtss, columns=dataset.columns)
print("\nDATA FRAME --------:\n", dtfrm)

xval = dataset.drop("Cumulative", axis=1)
yval = dataset["Cumulative"]

x_trn, x_tst, y_trn, y_tst = train_test_split(xval, yval, test_size = 0.2)
print("\nTrain :\n", x_trn)




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

agedrop = data.drop("age", axis=1)
datad = agedrop

stsclr = StandardScaler()
st = stsclr.fit_transform(datad)
yz = data["age"]

sttr, stts, yztr, yzts = train_test_split(st, yz, test_size=0.2)
print("\nTrain value :\n", sttr)
# print("\nTest value :\n", stts)
# print("\nYTrain value :\n", yztr)
# print("\nYTest value :\n", yzts)