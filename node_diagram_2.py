import os
import pandas as pd
from graphviz import Digraph
import shutil

df = pd.read_csv("G:\project\lisa_data\systemcall_selected\\0dcfa54a7e8a4e631ef466670ce604a61f3b0e8b3e9cf72c943278c0f77c31a2.out_converted.csv", index_col=0)
df = df.drop(['execname','pid'],axis=1)
column_number = df.shape[1]
row_number = df.shape[0] - 1
open_file_list = []
open_list_all = []
open_list_all_index = []

tmp_record_all = []
index_all = []
name_all = []
goodlist = list(range(row_number))
for i in range(0,row_number-1):
    combine_arg = df.iloc[i]['arguments'].replace(' ','').split(',')
    combine_arg.append(df.iloc[i]['return'])
    combine_arg = list(set(combine_arg))
    # print(combine_arg)
    for eachone in combine_arg:
        if eachone.startswith("0x") and eachone != "0x0" and eachone != "0x1" and i in goodlist:
            # print("Yes")
            tmp_name = []
            tmp_name.append(df.iloc[i]['name'])
            tmp_record = []
            tmp_record.append(eachone)
            index_record = []
            index_record.append(i)
            # print("i",i)
            for j in range(i+1,row_number):
                # print("j",j)
                combine_arg_tmp = df.iloc[j]['arguments'].replace(' ', '').split(',')
                combine_arg_tmp.append(df.iloc[j]['return'])
                combine_arg_tmp = list(set(combine_arg_tmp))
                # print(combine_arg_tmp)
                for eachone_j in combine_arg_tmp:
                    if eachone_j.startswith("0x") and eachone_j != "0x0" and eachone_j != "0x1" and -73728<=(eval(eachone) - eval(eachone_j))<=73728 and j in goodlist:
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


print(tmp_record_all)
print(index_all)
print(name_all)


