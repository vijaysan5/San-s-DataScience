# input > yelp.csv
# use TfidfVectorizer >>> fit_transform
# dataframe and kmeans cluster and use plots

import pandas as pan
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as mtpy

dts = pan.read_csv("San's  DataScience Folder/001 ds excel csv files/yelp.csv")

tfv = TfidfVectorizer()
fit = tfv.fit_transform(dts["text"])
print(fit)

df = pan.DataFrame(fit.toarray(), columns=tfv.get_feature_names_out())
print(df)

kmn = KMeans(n_clusters=2, random_state=43)
dts["cluster"] = kmn.fit_predict(fit)

clust = dts["cluster"].value_counts().sort_index()
mtpy.bar(clust.index, clust.values, color=["lightblue", "lightpink"])
mtpy.xticks([0,1])
mtpy.show()


# NLP and Wordcloud  >>> imp wc ===> from wordcloud import WordCloud
## use nltk.corpus >>>  nltk.download("stopwords")
## next plot
import pandas as pan
import matplotlib.pyplot as mtpy
import nltk
import string
from wordcloud import WordCloud
from nltk.corpus import stopwords

# nltk.download("stopwords")

