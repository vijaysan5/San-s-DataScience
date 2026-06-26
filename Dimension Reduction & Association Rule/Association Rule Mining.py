#Association rule mining

import pandas as pan
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori,association_rules

data = pan.read_csv("D:\Sangavi A\San's  DataScience Folder\\001 ds excel csv files\\starbucks_bakery_nutrition_clean.csv")
# print("Dataset :\n", data)
trans = data["Category"].apply(lambda x:x.split(","))
# print(trans)

Ten = TransactionEncoder()
Tencode = Ten.fit_transform(trans)
data_enc = pan.DataFrame(Tencode,columns=Ten.columns_)
print("Data Frame :\n", data_enc)

frequent = apriori(data_enc,min_support=0.05,use_colnames=True)
Rule = association_rules(frequent,metric="lift",min_threshold=1)

print("Rule------- :\n", Rule[["antecedents","consequents","support","confidence","lift"]].sort_values(by="lift", ascending=False).head(10))

