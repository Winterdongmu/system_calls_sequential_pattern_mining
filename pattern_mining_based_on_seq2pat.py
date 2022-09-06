import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import ast
df = pd.read_csv("G:\project\lisa_data\signature_based_on_seq2pat.csv", index_col=0)
sequence_list = df['sequence']
file_list = df['file']
new_sequence_list = []
for i in sequence_list:
    print(i)
    new_sequence_list.append(ast.literal_eval(i))
new_file_list = []
for i in file_list:
    new_file_list.append(list(set(ast.literal_eval(i))))

print(len(new_file_list))
tr = TransactionEncoder()
tr_arr = tr.fit(new_file_list).transform(new_file_list)
df = pd.DataFrame(tr_arr, columns=tr.columns_)
#print(df)
frequent_itemsets = apriori(df, min_support = 0.04, use_colnames = True)
original_list = []
support_list = []
for item in frequent_itemsets["itemsets"]:
    original_list.append(list(item))
for item in frequent_itemsets["support"]:
    support_list.append(item)
print(len(support_list))
print(len(original_list))
pattern = []
for i in original_list:
    for j in range(len(i)):
        i_tmp = i[:]

        i_tmp.pop(j)
        # print(i_tmp)
        if i_tmp in pattern and i in pattern:
            index = pattern.index(i_tmp)
            pattern.pop(index)
            # pattern.append(i)
        elif i_tmp in pattern and i not in pattern:
            index = pattern.index(i_tmp)
            pattern.pop(index)
            pattern.append(i)
        elif i not in pattern:
            # print(i)
            pattern.append(i)
# print(pattern)
print(len(pattern))

df2 = pd.DataFrame(pattern)
df2.to_csv("frequent_itemsets_apriori_filtered_seq2pat.csv")