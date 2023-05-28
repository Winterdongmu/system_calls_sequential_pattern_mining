import os
import pandas as pd
from graphviz import Digraph
import shutil

df = pd.read_csv(
    "G:\project\lisa_data\systemcall_selected\\0dcfa54a7e8a4e631ef466670ce604a61f3b0e8b3e9cf72c943278c0f77c31a2.out_converted.csv",
    index_col=0)
df = pd.read_csv(
    "G:\project\lisa_data\systemcall_selected\\53046ec20ff41109e92ae74a5d9ea300d01c07d08fff936f2c7f527cae6384ec.out_converted.csv",
    index_col=0)
df = df.drop(['execname', 'pid'], axis=1)
column_number = df.shape[1]
row_number = df.shape[0] - 1

dot = Digraph(name="System Call Flow", comment="test", format="png")

# Step 1: Find connections using memory address
tmp_record_all = []
index_all = []
name_all = []
goodlist = list(range(row_number))
for i in range(0, row_number - 1):
    combine_arg = str(df.iloc[i]['arguments']).replace(' ', '').split(',')
    combine_arg.append(df.iloc[i]['return'])
    combine_arg = list(set(combine_arg))
    # print(combine_arg)
    for eachone in combine_arg:
        eachone = str(eachone)
        if eachone.startswith("0x") and eachone != "0x0" and eachone != "0x1" and i in goodlist:
            # print("Yes")
            tmp_name = []
            tmp_name.append(df.iloc[i]['name'])
            tmp_record = []
            tmp_record.append(eachone)
            index_record = []
            index_record.append(i)
            # print("i",i)
            for j in range(i + 1, row_number):
                # print("j",j)
                combine_arg_tmp = str(df.iloc[j]['arguments']).replace(' ', '').split(',')
                combine_arg_tmp.append(df.iloc[j]['return'])
                combine_arg_tmp = list(set(combine_arg_tmp))
                # print(combine_arg_tmp)
                for eachone_j in combine_arg_tmp:
                    eachone_j = str(eachone_j)
                    if eachone_j.startswith("0x") and eachone_j != "0x0" and eachone_j != "0x1" and -73728 <= (
                            eval(eachone) - eval(eachone_j)) <= 73728 and j in goodlist:
                        # print(j)
                        tmp_record.append(eachone_j)
                        index_record.append(j)
                        tmp_name.append(df.iloc[j]['name'])
                        eachone = eachone_j
                        goodlist.remove(j)
                        # print(tmp_record)
            tmp_record_all.append(tmp_record)
            index_all.append(index_record)
            name_all.append(tmp_name)
            # print(tmp_record)
            # print(index_record)

# Give labels and edges to those connections found by memory address.
for i in range(len(name_all)):
    for j in range(len(name_all[i])):
        boxlabel = name_all[i][j]
        dot.node(name=str(index_all[i][j]), label=boxlabel, shape='box')

for i in range(len(name_all)):
    for j in range(len(name_all[i]) - 1):
        culculate_value = eval(tmp_record_all[i][j]) - eval(tmp_record_all[i][j + 1])
        dot.edge(tail_name=str(index_all[i][j]), head_name=str(index_all[i][j + 1]), label=str(culculate_value))



# Step 2: Find connections using file related system calls
open_file_list = []
open_list_all = []
open_list_all_index = []
for i in range(0, row_number):
    if (df.iloc[i]['name'] == 'open' or df.iloc[i]['name'] == 'openat') and df.iloc[i]['return'] != "-2 (ENOENT)":
        if df.iloc[i]['name'] == 'open':
            open_file_list.append(df.iloc[i]['arguments'].split(',')[0])
        else:
            open_file_list.append(df.iloc[i]['arguments'].split(',')[1])
        tmp_file_return = df.iloc[i]['return']
        open_list = []
        open_list_index = []
        open_list.append(df.iloc[i]['name'])
        open_list_index.append(i)
        for j in range(i, row_number):
            if str(df.iloc[j]['arguments']).split(',')[0] == tmp_file_return:
                if df.iloc[j]['name'] != "close":
                    open_list.append(df.iloc[j]['name'])
                    open_list_index.append(j)
                else:
                    open_list.append('close')
                    open_list_index.append(j)
                    break
        open_list_all.append(open_list)
        open_list_all_index.append(open_list_index)
print(open_list_all)
print(open_list_all_index)

# Give labels and edges to those connections found by file descriptors.
for i in range(len(open_list_all)):
    for j in range(len(open_list_all[i])):
        if open_list_all[i][j] == 'open' or open_list_all[i][j] == 'openat':
            boxlabel = open_list_all[i][j] + '\n' + open_file_list[i]
        else:
            boxlabel = open_list_all[i][j]
        dot.node(name=str(open_list_all_index[i][j]), label=boxlabel, shape='box')

for i in range(len(open_list_all)):
    for j in range(len(open_list_all[i]) - 1):
        dot.edge(tail_name=str(open_list_all_index[i][j]), head_name=str(open_list_all_index[i][j + 1]))

print(dot.source)
dot.render('test-output/test-table9', view=True)


