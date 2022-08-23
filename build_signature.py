import pandas as pd
import numpy as np
import ast
from sequential.seq2pat import Seq2Pat, Attribute
df = pd.read_csv("G:\project\lisa_data\pattern_dict_list.csv", index_col=0)
df2 = pd.read_csv("G:\project\lisa_data\Lin_code\\frequent_itemsets_apriori_filtered.csv", index_col=0)
sequence_list = df['sequence']
file_list = df['file']
new_sequence_list = []
for i in sequence_list:
    new_sequence_list.append(ast.literal_eval(i))
new_file_list = []
for i in file_list:
    new_file_list.append(list(set(ast.literal_eval(i))))
# print(df.values)
itemset = df2.values.tolist()
for i in itemset:
    while np.nan in i:
        i.remove(np.nan)

filter_number = 5
filter_list = []
for i in itemset:
    if len(i) >= 5:
        filter_list.append(i)
print(filter_list)
signature_dict_list = []
for i in filter_list:
    sequence_store = []
    for j in new_file_list:
        tmp_list = list(set(i)&set(j))
        mark = True
        for k in i:
            if k not in tmp_list:
                mark = False
        if mark ==True:
            sequence_store.append(new_sequence_list[new_file_list.index(j)])

    signature_info = {
        'file': i,
        'sequence': sequence_store,
    }
    signature_dict_list.append(signature_info)
print(signature_dict_list)