import os,sys,csv
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

import pandas as pd
import numpy as np
import ast
import copy
from sequential.seq2pat import Seq2Pat, Attribute

df = pd.read_csv("G:\project\lisa_data\pattern_dict_list.csv", index_col=0)
sequence_list = df['sequence']
file_list = df['file']
count_list = df['count']
# sequence_list = np.array(df['sequence'])
# sequence_list = sequence_list.reshape(1, len(sequence_list)).tolist()
# print(sequence_list)
# print(file_list)

new_sequence_list = []
for i in sequence_list:
    new_sequence_list.append(ast.literal_eval(i))
new_file_list = []
for i in file_list:
    new_file_list.append(list(set(ast.literal_eval(i))))
new_count_list = []
for i in count_list:
    new_count_list.append(i)


syscall_dict_list = []
for i in range(len(new_sequence_list)):
    syscall_info = {
        'sequence': new_sequence_list[i],
        'count':new_count_list[i],
        'file': new_file_list[i]
    }
    syscall_dict_list.append(syscall_info)
df = pd.DataFrame(syscall_dict_list)
df.to_csv("Simplified_pattern_dictionary.csv")
