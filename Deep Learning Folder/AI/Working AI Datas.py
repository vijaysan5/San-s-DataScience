import pandas as pan
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

"Read Dataset :---"
Bank = pan.read("San's  DataScience Folder/000 ds csv files/bank-data.csv")

Bank = Bank.replace("?", pan.NA)
Bank = Bank.dropna()

len = LabelEncoder()
for bk in Bank.columns:
    if Bank[bk].dtype == "object" :
        Bank[bk] = len.fit_transform(Bank[bk])