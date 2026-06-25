import pandas as pan
import matplotlib.pyplot as mtpy
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data = pan.read_csv("San's  DataScience Folder/001 ds excel csv files/fx_rate_2010_2019.csv")

dr = data.drop(['date'], axis=1)
print(dr)

trns = StandardScaler().fit_transform(dr)
print(trns)

pca = PCA(n_components=2)
fit = pca.fit_transform(trns)
print(fit)

mtpy.scatter(fit[:,0], fit[:,1])
mtpy.show()