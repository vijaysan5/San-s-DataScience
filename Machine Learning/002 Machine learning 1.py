
# Unsupervised learning  ==> Sklearn - Preprocessing >>> KMeans with plot
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


""" import pandas as pan 
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder

image = pan.read_csv("San's  DataScience Folder\\000 ds csv files\image_dataset.csv")
img = image.drop(["image"], axis=1)

lben = LabelEncoder()
img["labels"] = lben.fit_transform(img["labels"])
ss = StandardScaler()
ss.fit_transform(img)

kmn = KMeans(n_clusters=2, random_state=42)
image["k-clusters"] = kmn.fit_predict(img)
prnt = image[["labels", "k-clusters"]]
print(prnt) """




print("\n----------------------------------------------------------------------------")
print("----------------------------------------------------------------------------\n")
# Unsupervised learning  ==> Scipy - Cluster - Hierarchy with plot (Dendrogram)
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