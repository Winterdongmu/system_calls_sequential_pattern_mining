import pandas as pd
import numpy as np
import ast
from sequential.seq2pat import Seq2Pat, Attribute
df = pd.read_csv("G:\project\lisa_data\Simplified_pattern_dictionary.csv", index_col=0)
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

filter_number = 6
filter_list = []
for i in itemset:
    if len(i) >= filter_number:
        filter_list.append(i)
# print(filter_list)

# print(len(new_file_list))
# print(set(new_file_list))
# print(len(list(set(new_file_list))))
signature_dict_list = []
tmp_filename_list = []
tmp_sequence_list = []
for i in filter_list:
    sequence_store = []
    for j in range(len(new_file_list)):
        tmp_list = list(set(i)&set(new_file_list[j]))
        mark = True
        for k in i:
            if k not in tmp_list:
                mark = False
        if mark ==True:
            # print(j)
            # print(new_sequence_list[new_file_list.index(j)])
            sequence_store.append(new_sequence_list[j])


    signature_info = {
        'file': i,
        'sequence': sequence_store,
    }
    tmp_filename_list.append(i)
    tmp_sequence_list.append(sequence_store)
    signature_dict_list.append(signature_info)

df3 = pd.DataFrame(signature_dict_list)
df3.to_csv("signature.csv")
print(tmp_sequence_list)
index_list_tmp = []
signature_info_filter_list = []
for i in range(len(tmp_sequence_list)):
    if i not in index_list_tmp:
        index_list_tmp_tmp = []
        index_list_tmp_tmp.append(i)
        for j in range(i+1,len(tmp_sequence_list)):
            if j not in index_list_tmp:
                if tmp_sequence_list[i] == tmp_sequence_list[j]:
                    # tmp_filename_list[i] = list(set(tmp_filename_list[i] + tmp_filename_list[j]))
                    index_list_tmp.append(j)
                    index_list_tmp_tmp.append(j)
        newlist_file_name = []
        for index in index_list_tmp_tmp:
            newlist_file_name = list(set(newlist_file_name + tmp_filename_list[index]))
        signature_info_filter = {
            'file': newlist_file_name,
            'sequence': tmp_sequence_list[i],
        }
        signature_info_filter_list.append(signature_info_filter)
# print(signature_info_filter_list)
df4 = pd.DataFrame(signature_info_filter_list)
df4.to_csv("signature_filtered.csv")