from sequential.seq2pat import Seq2Pat, Attribute
import numpy as np
import os
import pandas as pd
import operator
import copy
# df = pd.read_csv("G:\project\lisa_data\seq2pat_pattern_list_original.csv", index_col=0, low_memory=False)
# itemset = df.values.tolist()
# for i in itemset:
#     while np.nan in i:
#         i.remove(np.nan)
# print(itemset)
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
seq2pat = Seq2Pat(list_all,max_span=2400)
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

# tmp_list = copy.deepcopy(results_2)
# tmp_tmp = copy.deepcopy(tmp_list)
# print(tmp_tmp)
# print(tmp_list)


pattern = []
tmp_pattern = []
print(len(results_2))
for i in range(len(results_2)):
    if i not in tmp_pattern:
        print(i)
        i_mark = True
        range_k = i+50
        if range_k > len(results_2):
            range_k = len(results_2)
        for j in range(i+1,len(results_2)):
            if j not in tmp_pattern:
                if set(results_2[i]).issubset(set(results_2[j])):
                    tmp_length = len(results_2[i])
                    pos_list = [k for k, x in enumerate(results_2[j]) if x == results_2[i][0]]
                    for index in pos_list:
                        if results_2[j][index:index + tmp_length] == results_2[i] and (index + tmp_length) <= len(results_2[j]) and count_list[j] == count_list[i]:
                            if results_2[i] in pattern:
                                tmp_index = pattern.index(results_2[i])
                                pattern.pop(tmp_index)

                            # print(j)
                            pattern.append(results_2[j])
                            results_2[i] = results_2[j]
                            tmp_pattern.append(j)
                            # print(len(tmp_pattern))

                            # print(tmp_pattern)
                            i_mark = False
                            break
        if i_mark == True and results_2[i] not in pattern:
            pattern.append(results_2[i])
            tmp_pattern.append(i)
#
# pattern = []
# for i in results_2:
#     filter_list = [0,-1]
#     for j in filter_list:
#         i_tmp = i[:]
#
#         i_tmp.pop(j)
#         # print(i_tmp)
#         if i_tmp in pattern and i in pattern:
#             index = pattern.index(i_tmp)
#             pattern.pop(index)
#             # pattern.append(i)
#         elif i_tmp in pattern and i not in pattern:
#             index = pattern.index(i_tmp)
#             pattern.pop(index)
#             pattern.append(i)
#         elif i not in pattern:
#             # print(i)
#             pattern.append(i)
#
#
#
#

# results_3 = copy.deepcopy(pattern)
# results_3 = list(reversed(results_3))
# new_pattern = []
# for i in results_3:
#     filter_list = [0, -1]
#     for j in filter_list:
#         i_tmp = i[:]
#
#         i_tmp.pop(j)
#         # print(i_tmp)
#         if i_tmp in new_pattern and i in new_pattern:
#             index = new_pattern.index(i_tmp)
#             new_pattern.pop(index)
#             # pattern.append(i)
#         elif i_tmp in new_pattern and i not in new_pattern:
#             index = new_pattern.index(i_tmp)
#             new_pattern.pop(index)
#             i_index = results_3.index(i)
#             i.append(count_list[i_index])
#             new_pattern.append(i)
#         elif i not in new_pattern:
#             # print(i)
#             index = results_3.index(i)
#             i.append(count_list[index])
#             new_pattern.append(i)
#
# new_pattern = list(reversed(new_pattern))
print(len(pattern))
# pattern = list(set([tuple(t) for t in pattern]))

pattern_list_with_count = copy.deepcopy(pattern)
for i in pattern_list_with_count:
    i.append(count_list[results_2.index(i)])


# print(len(pattern))
# pattern = list(set([tuple(t) for t in pattern]))
print(len(pattern))
# pattern=list(set(pattern))
df1 = pd.DataFrame(results)
df1.to_csv("seq2pat_pattern_list_original.csv")
df2 = pd.DataFrame(pattern)
df2.to_csv("seq2pat_pattern_list_plus.csv")
df3 = pd.DataFrame(pattern_list_with_count)
df3.to_csv("seq2pat_pattern_list_plus_with_count.csv")
