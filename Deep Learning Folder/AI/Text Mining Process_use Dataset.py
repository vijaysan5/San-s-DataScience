import pandas as pan
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

Dataset = pan.read_csv("San's  DataScience Folder/001 ds excel csv files/fake reviews dataset.csv")
Labs = [
    "CG",
    "OR"
]

vector = CountVectorizer()
Trans = vector.transform(Dataset)

MultiNB = MultinomialNB()
MultiNB.fit(Trans, Labs)

Test = ["Love this! Well made, sturdy, and very comfortable.  I love it!Very pretty"]

T_Data = vector.fit_transform(Test)
Predict = MultiNB.predict(T_Data)

print("Test line :", Test[0])
print("Predict   :", Predict[0])
print("Completed...")