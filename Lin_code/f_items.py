import os,sys,csv
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

dataset=[] #without bonus

cpt=0
with open("649.csv","r") as file:
	csvreader = csv.reader(file)
	for row in csvreader:
		if cpt!=0:
			r=[row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
			dataset.append(r)
		else:
			cpt=cpt+1
print(dataset)

tr = TransactionEncoder()
tr_arr = tr.fit(dataset).transform(dataset)
df = pd.DataFrame(tr_arr, columns=tr.columns_)
#print(df)
frequent_itemsets = apriori(df, min_support = 0.01, use_colnames = True) # 2%-13%: 0.1, 1%
#frequent_itemsets = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
cpt=0
for item in frequent_itemsets["itemsets"]:
	print(list(item))
	# if len(item)>3:
		# cpt=cpt+1
# print(cpt)