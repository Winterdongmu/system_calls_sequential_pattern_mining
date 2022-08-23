from sequential.seq2pat import Seq2Pat, Attribute
import os
import pandas as pd
import operator
import copy
path = "G:\project\lisa_data\syscall_test_2"

list_all = []
file_all = []
for filename in os.listdir(path):
    realfilename = os.path.join(path, filename)
    # print(realfilename)
    df = pd.read_csv(realfilename)
    list_all.append(df['name'].tolist())
    file_all.append(filename)
# print(list_all[0])

list_length_all = len(list_all)
pattern_list = []
# pattern_dict = {}
pattern_dict_list = []
# print(list_all[0])
# print(file_all[0])
seq2pat = Seq2Pat(list_all)
# syscall = Attribute(list_all)

index_list = []
for i in range(0,len(list_all)):
    new_list = list(range(0,len(list_all[i])))
    index_list.append(new_list)
timestamp = Attribute(index_list)
gap_constraint = seq2pat.add_constraint(0 <= timestamp.gap() <= 1)
results = seq2pat.get_patterns(min_frequency=11)
print(results)

results_2 = copy.deepcopy(results)
count_list = []
for i in results_2:
    count_list.append(i.pop())
print(results_2)
tmp_list = copy.deepcopy(results_2)
tmp_tmp = copy.deepcopy(tmp_list)
# print(tmp_tmp)
# print(tmp_list)
signal = False

row_number = list(range(len(tmp_tmp)))

signal = False
while signal == False:
    tmp_length = len(tmp_tmp)
    for i in row_number:
        # print(i)
        # print(tmp_list[i])
        tmp_list[i].pop()
        tmp_value = tmp_list[i]
        # print("tmp_value:",tmp_value)
        if tmp_value in tmp_tmp:
            tmp_index = tmp_tmp.index(tmp_value)
            tmp_tmp.pop(tmp_index)
            count_list.pop(tmp_index)
            tmp_list = []
            tmp_list = copy.deepcopy(tmp_tmp)
            row_number.pop()
        # print(tmp_tmp)
    if tmp_length == len(tmp_tmp):
        signal = True


for i in range(len(tmp_tmp)):
    tmp_tmp[i].append(count_list[i])
print(tmp_tmp)

df1 = pd.DataFrame(results)
df1.to_csv("seq2pat_pattern_list_original.csv")
df2 = pd.DataFrame(tmp_tmp)
df2.to_csv("seq2pat_pattern_list_plus.csv")