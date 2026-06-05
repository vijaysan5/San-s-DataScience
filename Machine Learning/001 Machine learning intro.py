# Use Gaussian NB
""" 
import pandas as pan
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

house = pan.read_csv("San's  DataScience Folder\\000 ds csv files\Housing_Data.csv")
# print("Reading Dataset :\n", house)
housecopy = house.copy()

lben = LabelEncoder()
housecopy["Index"] = lben.fit_transform(housecopy["Index"])
housecopy["driveway"] = lben.fit_transform(housecopy["driveway"])
housecopy["recroom"] = lben.fit_transform(housecopy["recroom"])
housecopy["fullbase"] = lben.fit_transform(housecopy["fullbase"])
housecopy["gashw"] = lben.fit_transform(housecopy["gashw"])
housecopy["airco"] = lben.fit_transform(housecopy["airco"])
housecopy["prefarea"] = lben.fit_transform(housecopy["prefarea"])
# drop
droping = housecopy.drop(["driveway"], axis=1)
x = droping
y = housecopy["driveway"]
# train test split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=50)
print("xtrain :---", xtrain)

gsnb = GaussianNB()
gsnb.fit(xtrain, ytrain)
print("xtest :---", xtest)

prob = gsnb.predict(xtest)
print("Prob :---", prob)
# print("ytest :---", ytest)

accur = accuracy_score(prob, ytest)
print("Accuracy :---", accur)


testfile = {
    "Index" : 49.0,
    "price" : 32.0,
    "lotsize" : 43.5,
    "bedrooms" : 27.0,
    "bathrms" : 32.0,
    "stories" : 40.0,
    "recroom" : 34.0,
    "fullbase" : 37.0,
    "gashw" : 48.0,
    "airco" : 39.0,
    "garagepl" : 38.0,
    "prefarea" : 39.0
}

dfrm = pan.DataFrame([testfile])
file = gsnb.predict(dfrm)
print("dfrm Predict :\n" , file[0])

 """

import pandas as pan 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

emp = pan.read_csv("San's  DataScience Folder\\000 ds csv files\Employee data.csv")
# print("Employee Data CSV :\n", emp)
emc = emp.copy()

lben = LabelEncoder()
emc["minority"] = lben.fit_transform(emc["minority"])
emc["gender"] = lben.fit_transform(emc["gender"])
emc["jobcat"] = lben.fit_transform(emc["jobcat"])
emc["bdate"] = lben.fit_transform(emc["bdate"])
emc["prevexp"] = lben.fit_transform(emc["prevexp"])

# drop
drp = emc.drop(["minority"], axis=1)

xval = drp
yval = emc["minority"]
print("xval :", xval)
print("yval :", yval)

xtrn, xtst, ytrn, ytst = train_test_split(xval, yval, test_size=0.2, random_state=40)
print("Train :", xtrn)

ranf = RandomForestClassifier()
ranf.fit(xtrn, ytrn)
print("\n X Testing :\n", xtst)

Prob = ranf.predict(xtst)
print("\nProb :", Prob)

acc_score = accuracy_score(Prob, ytst)
print("\nAccuracy Score :\n", acc_score)


test = {
    "id" : 20.0,
    "gender" : 43.0,
    "bdate" : 70.0,
    "educ" : 40.3,
    "jobcat" : 34.0,
    "salary" : 90.0,
    "salbegin" : 84.0,
    "jobtime" : 99,
    "prevexp" : 100,
}

dataf = pan.DataFrame([test])
Predict = ranf.predict(dataf)
print("Emp pred :", Predict)