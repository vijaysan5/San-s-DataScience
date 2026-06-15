""" import pandas as pan 
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as mtpy

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

km = KMeans(n_clusters=2, random_state=42)
baskin['k-cluster'] = km.fit_predict(bsk)
bbs = baskin[["minority","k-cluster"]]

df = pan.DataFrame(bbs)
csv_data = df.to_csv("emp minority.csv", index=False)
print("Created csv") """

import pandas as pan 
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
print(prnt)

# df = pan.DataFrame(prnt)
# csv_data = df.to_csv("Yes or No data.csv", index=False)
# print("Created csv")

df = pan.DataFrame(prnt)
# csv_data = df.to_csv("Yes or No data.csv", index=False)
# print("Created csv")

read = pan.read_csv("Yes or No data.csv")

x = read["k-clusters"[0]]
y = read["k-clusters"[1]]