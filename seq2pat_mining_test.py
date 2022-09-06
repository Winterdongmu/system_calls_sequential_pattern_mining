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
def find_the_longest(results_3,new_count):
    second_pattern = []
    tmp_pattern = []
    for i in range(len(results_3)):
        if i not in tmp_pattern:
            # print(i)
            i_mark = True
            for j in range(i + 1, len(results_3)):
                if j not in tmp_pattern:
                    if set(results_3[i]).issubset(set(results_3[j])):
                        tmp_length = len(results_3[i])
                        pos_list = [k for k, x in enumerate(results_3[j]) if x == results_3[i][0]]
                        for index in pos_list:
                            if results_3[j][index:index + tmp_length] == results_3[i] and (index + tmp_length) <= len(
                                    results_3[j]) and new_count[j] == new_count[i]:
                                if results_3[i] in second_pattern:
                                    tmp_index = second_pattern.index(results_3[i])
                                    second_pattern.pop(tmp_index)

                                # print(j)
                                second_pattern.append(results_3[j])
                                results_3[i] = results_3[j]
                                tmp_pattern.append(j)
                                # print(len(tmp_pattern))

                                # print(tmp_pattern)
                                i_mark = False
                                break
            if i_mark == True and results_3[i] not in second_pattern:
                second_pattern.append(results_3[i])
                tmp_pattern.append(i)
    return second_pattern
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
# print(results)

results_2 = copy.deepcopy(results)
count_list = []
for i in results_2:
    count_list.append(i.pop())
# print(results_2)

# tmp_list = copy.deepcopy(results_2)
# tmp_tmp = copy.deepcopy(tmp_list)
# print(tmp_tmp)
# print(tmp_list)
print(len(results_2))
print(len(count_list))
first_pattern = []
new_count = []
for i in range(0,len(results_2)-1):
    tmp_mark = True
    tmp_store_list = copy.deepcopy(results_2[i+1])
    tmp_store_list.pop()
    if tmp_store_list== results_2[i]:
        tmp_mark = False

    if tmp_mark == True:
        first_pattern.append(results_2[i])
        new_count.append(count_list[i])

print("first:",len(first_pattern))
print(len(count_list))

results_3 = copy.deepcopy(first_pattern)
second_pattern = find_the_longest(results_3,new_count)

print(len(second_pattern))
# pattern = list(set([tuple(t) for t in second_pattern]))
# print(len(pattern))
new_count_2 = []
for i in second_pattern:
    new_count_2.append(new_count[first_pattern.index(i)])

results_4 = copy.deepcopy(second_pattern)
new_count_3 = copy.deepcopy(new_count_2)
results_5 = list(reversed(results_4))
new_count_4 = list(reversed(new_count_3))

third_pattern = find_the_longest(results_5,new_count_4)
third_pattern = list(reversed(third_pattern))
new_count_5 = list(reversed(new_count_4))
new_count_6 = []
for i in third_pattern:
    new_count_6.append(new_count_5[second_pattern.index(i)])
print(len(third_pattern))
print(len(new_count_6))

fourth_pattern = copy.deepcopy(third_pattern)
for i in range(len(fourth_pattern)):
    fourth_pattern[i].append(new_count_6[i])

df1 = pd.DataFrame(first_pattern)
df1.to_csv("seq2pat_first_pattern_test.csv")
df2 = pd.DataFrame(second_pattern)
df2.to_csv("seq2pat_second_pattern_test.csv")
df3 = pd.DataFrame(third_pattern)
df3.to_csv("seq2pat_third_pattern_test.csv")
df4 = pd.DataFrame(fourth_pattern)
df4.to_csv("seq2pat_fourth_pattern_test.csv")


# pattern_list_with_count = copy.deepcopy(pattern)
# for i in pattern_list_with_count:
#     i.append(count_list[results_2.index(i)])
#
#
# # print(len(pattern))
# # pattern = list(set([tuple(t) for t in pattern]))
# print(len(pattern))
# # pattern=list(set(pattern))
# df1 = pd.DataFrame(results)
# df1.to_csv("seq2pat_pattern_list_original.csv")
# df2 = pd.DataFrame(pattern)
# df2.to_csv("seq2pat_pattern_list_plus.csv")
# df3 = pd.DataFrame(pattern_list_with_count)
# df3.to_csv("seq2pat_pattern_list_plus_with_count.csv")
