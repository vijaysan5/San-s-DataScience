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
# print("read----------------")
r_f = pan.read_csv("San's  DataScience Folder/001 ds excel csv files/real and fake reviews ds.csv")
print("Read this file-----------")
# print("Lable :\n", r_f["label"])

def cleant(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tkn = text.split()
    print("Line : ",end=" ")
    tkn = [wdcd for wdcd in tkn if wdcd not in stopwords.words('english')]
    print(" 1 ")
    return " ".join(tkn)

r_f["Cleantx"] = r_f["text"].apply(cleant)
print(r_f["Cleantx"])

Real = " ".join(r_f[r_f["label"] == "REAL"]["Cleantx"])
Fake = " ".join(r_f[r_f["label"] == "FAKE"]["Cleantx"])

rwc = WordCloud(width=800, height=400, background_color="lightblue", colormap="Reds").generate(Real)
fwc = WordCloud(width=800, height=400, background_color="lightgreen", colormap="Reds").generate(Fake)

mtpy.subplot(1,2,1)
mtpy.imshow(rwc)
mtpy.subplot(1,2,2)
mtpy.imshow(fwc)
# mtpy.tight_layout()
mtpy.show()



# Time Series > Data Analysis
import pandas as pan
import matplotlib.pyplot as mtpy

dts = pan.read_csv("San's  DataScience Folder/001 ds excel csv files/time-series-data.csv")
print("Dataset :", dts.head())

# flow >>> dts["flow"] using plot
mtpy.plot(dts["timestamp"], dts["flow"], color="Red")
mtpy.show()

# temp >>> dts["temp"] using plot
mtpy.plot(dts["timestamp"], dts["temp"], color="green")
mtpy.show()