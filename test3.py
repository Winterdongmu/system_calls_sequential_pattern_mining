import os
import pandas as pd
path = "G:\project\lisa_data\syscall_test_2"

find_list = ['pipe2', 'write']
list_all = []
file_all = []
for filename in os.listdir(path):
    realfilename = os.path.join(path, filename)
    # print(realfilename)
    df = pd.read_csv(realfilename)
    list_all.append(df['name'].tolist())
    file_all.append(filename)
count = 0
for j in range(len(list_all)):
    if set(find_list).issubset(set(list_all[j])):
        tmp_length = len(find_list)
        pos_list = [k for k, x in enumerate(list_all[j]) if x == find_list[0]]
        for index in pos_list:
            if list_all[j][index:index+tmp_length] == find_list and (index+tmp_length) <= len(list_all[j]):
                count+=1
                break

print(count)