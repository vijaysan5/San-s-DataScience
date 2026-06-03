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
