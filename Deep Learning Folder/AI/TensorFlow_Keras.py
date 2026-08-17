import pandas as pan
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

"Read Dataset :"
Data = pan.read_csv("D:\Sangavi A\San's  DataScience Folder\\000 ds csv files\Adult csv file.csv")

"Remove Missing Values :--"
Data = Data.replace("?", pan.NA)
Data = Data.dropna()

"Encode Categorical Columns :--"
len = LabelEncoder()
for clmn in Data.columns :
    if Data[clmn].dtype == "object" :
        Data[clmn] = len.fit_transform(Data[clmn])

"Features and Target :--"
ab = Data.drop("income", axis=1)
xy = Data["income"]

"Sclae Futures :--"
scl = StandardScaler()
ab = scl.fit_transform(ab)

"Split Data :---"
ab_train, ab_test, xy_train, xy_test = train_test_split(
    ab, xy, test_size=0.2, random_state=42
)

"Build Tensor Flow Model :---"
tf_model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

"Compile :---"
tf_model.compile(
    optimizer = "adam",
    loss = "binary_crossentropy",
    metrics = ["accuracy"]
)

tf_model.fit(ab_train, xy_train, epochs = 10, batch_size = 32)

"Evaluate :---"
loss, accuracy = tf_model.evaluate(ab_test, xy_test)

print("Accuracy :===>", accuracy)





# Tens :===>>><<<
import pandas as pan
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

ds = pan.read_csv("San's  DataScience Folder/000 ds csv files/Adult csv file.csv")

"Remove Missing Value :"
ds.replace("?", pan.NA, inplace=True)
ds.dropna(inplace=True)

"Encode :"
len = LabelEncoder()

for clmn in ds.columns :
    if ds[clmn].dtype == "object" :
        ds[clmn] = len.fit_transform(ds[clmn])

ax = ds.drop(["income"], axis = 1)
ay = ds["income"]




    