""" import pandas as pan 
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
print("\nProb :", prob) """


# Supervised learning  ==> Sklearn - Preprocessing >>> KMeans with plot
""" import pandas as pan 
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as mtpy

baskin = pan.read_csv("D:\Sangavi A\San's  DataScience Folder\\000 ds csv files\BaskinRobbins.csv")
bsk = baskin.drop(["Flavour"], axis=1)

ss = StandardScaler()
ss.fit_transform(bsk)

km = KMeans(n_clusters=3, random_state=42)
bsk['k-cluster'] = km.fit_predict(bsk)
print(bsk)

mtpy.scatter(bsk["Calories"], bsk["Sugars (g)"], c=bsk['k-cluster'], cmap="Set1",s=100, edgecolors="k")
mtpy.show() """

print("\n----------------------------------------------------------------------------")
print("----------------------------------------------------------------------------\n")
# Unsupervised learning  ==> Scipy - Cluster - Hierarchy with plot
""" "one----------" 
import matplotlib.pyplot as mtpy
import pandas as pan
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

adm = pan.read_csv("San's  DataScience Folder\\000 ds csv files\Admission_Predict.csv")
admc = adm.drop(["Serial No."], axis=1)

scal = StandardScaler()
xv = scal.fit_transform(admc)
link = linkage(xv, method='ward')

dendrogram(link, orientation='top', distance_sort="descenting")
mtpy.show()

"two----------"
zill = pan.read_csv("San's  DataScience Folder\\000 ds csv files\zillow.csv")
zillc = zill.drop(["Index"], axis=1)

yv = scal.fit_transform(zillc)
linked = linkage(yv, method='ward')

dendrogram(linked, orientation='top', distance_sort='descenting')
mtpy.show()
 """


# check (csv minority) (k-cluster)
""" import pandas as pan 
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder

baskin = pan.read_csv("San's  DataScience Folder\\000 ds csv files\Employee data.csv")
bsk = baskin.drop(["id"], axis=1)
lben = LabelEncoder()
bsk["minority"] = lben.fit_transform(bsk["minority"])
bsk["gender"] = lben.fit_transform(bsk["gender"])
bsk["jobcat"] = lben.fit_transform(bsk["jobcat"])
bsk["bdate"] = lben.fit_transform(bsk["bdate"])
bsk["prevexp"] = lben.fit_transform(bsk["prevexp"])

ss = StandardScaler()
ss.fit_transform(bsk)
km = KMeans(n_clusters=2, random_state=78)
baskin['k-cluster'] = km.fit_predict(bsk)
print(baskin[["minority","k-cluster"]])
 """


import pandas as pan 
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as mtpy
image = pan.read_csv("San's  DataScience Folder\\000 ds csv files\image_dataset.csv")
img = image.drop(["image"], axis=1)

lben = LabelEncoder()
img["labels"] = lben.fit_transform(img["labels"])
ss = StandardScaler()
ss.fit_transform(img)

kmn = KMeans(n_clusters=2, random_state=42)
image["k-clusters"] = kmn.fit_predict(img)
prnt = image[["labels", "k-clusters"]]
print(prnt)

