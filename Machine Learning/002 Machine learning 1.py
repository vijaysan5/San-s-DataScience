import pandas as pan 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

dt_org = pan.read_csv("San's  DataScience Folder\\000 ds csv files\Bags_Product.csv")
print(dt_org.info())

dataset = dt_org.copy()

obj_int = dataset.select_dtypes(include="object").columns

lben = LabelEncoder()
for x in obj_int:
    dataset[x] = lben.fit_transform(dataset[x])
# print(dataset.info())

drp = dataset.drop(["DIY"], axis=1)
xv = drp
yv = dataset["DIY"]

xtrain, xtest, ytrain, ytest = train_test_split(xv, yv, test_size=0.2, random_state=40)
# print("X Train", xtrain)

rdnc = RandomForestClassifier()
rdnc.fit(xtrain, ytrain)
# print("xtest :", xtest)

prb = rdnc.predict(xtest)
print("Prob :", prb)
print("\n----------------------------------------------------------------------------\n")

# Surface
from sklearn.linear_model import LinearRegression

add = pan.read_csv("San's  DataScience Folder\\000 ds csv files\Admission_Predict.csv")
# print("add info :\n", add.info())

cadd = add.copy()

xad = cadd.drop(["University Rating", "SOP"], axis=1)
yad = cadd["University Rating"]

xadtrain, xadtest, yadtrain, yadtest = train_test_split(xad, yad, test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(xadtrain, yadtrain)

prob = lr.predict(xadtest)
print("\nProb :", prob)