#Association rule mining

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori,association_rules

df=pd.read_csv("001 Ds___Datasets Folder/starbucks_bakery_nutrition_clean.csv")
# print(df)
transactions=df["Category"].apply(lambda x:x.split(","))
# print(transactions)


te=TransactionEncoder()
te_data=te.fit_transform(transactions)
df_encoded=pd.DataFrame(te_data,columns=te.columns_)
print("Encoded :\n", df_encoded)

freq=apriori(df_encoded,min_support=0.05,use_colnames=True)
rule=association_rules(freq,metric="lift",min_threshold=1)

print("Rule :\n", rule[["antecedents","consequents","support","confidence","lift"]]
      .sort_values(by="lift",ascending=False).head(10))