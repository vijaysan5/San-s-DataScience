import pandas as pan
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split



# data = pan.read_csv("San's  DataScience Folder\ds csv files\\student dataset_new.csv")
# print("CSV Info :\n", data.info())

# print("Null :\n", data.isna().sum())
# print("Duplicate :\n", data.duplicated().sum())
# datafix = data.ffill()
# print("null fix :\n", datafix.isna().sum)
# print("dup fix :\n", datafix.duplicated().sum())


dataset = pan.read_csv("San's  DataScience Folder\ds csv files\\effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv")
print("CSV Info :\n", dataset.info())

print("Null :\n", dataset.isna().sum())
print("Duplicate :\n", dataset.duplicated().sum())

# Change >>> Object to int64
cng_int = dataset.select_dtypes(include="object").columns
lben = LabelEncoder()
for x in cng_int:
    dataset[x] = lben.fit_transform(dataset[x])
print(dataset.info())

# Standards Scaler convert
stsclr = StandardScaler()
dtss = stsclr.fit_transform(dataset)
print("Standard Scaler --------:\n", dtss)

# Convert to Data Frame 
dtfrm = pan.DataFrame(dtss, columns=dataset.columns)
print("DATA FRAME --------:\n", dtfrm)

xval = dataset.drop("Cumulative", axis=1)
yval = dataset["Cumulative"]

x_trn, x_tst, y_trn, y_tst = train_test_split(xval, yval, test_size = 0.2)
print(x_trn)