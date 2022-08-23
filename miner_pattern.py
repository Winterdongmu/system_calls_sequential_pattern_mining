import os
import pandas as pd
import operator

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
for threshold in range(2,16):
    # threshold = 8
    print("\n")
    print("threshold:", threshold)
    compare_value = 11
    for first_index in range(0, list_length_all):
        # print("\n")
        # print("first_index:", first_index)
        first_list_length_single = len(list_all[first_index])
        for first_list_index in range(0, first_list_length_single - threshold):
            tmp_list = []
            for i in range(0, threshold):
                tmp_list.append(list_all[first_index][first_list_index + i])
            if tmp_list not in pattern_list:
                count = 0
                file_list = []
                file_list.append(file_all[first_index])
                for second_index in range(0, list_length_all):
                    # print("second_index:",second_index,"(",first_index,")")
                    if first_index != second_index:
                        second_list_length_single = len(list_all[second_index])
                        for second_list_index in range(0, second_list_length_single - threshold):
                            tmp_list_2 = []
                            for i in range(0, threshold):
                                tmp_list_2.append(list_all[second_index][second_list_index + i])

                            if operator.eq(tmp_list, tmp_list_2):
                                count += 1
                                file_list.append(file_all[second_index])
                if count >= compare_value:
                    tmp_list_3 = tmp_list[:]
                    tmp_list_3.pop()
                    break_sign = False

                    syscall_info = {
                        'sequence': tmp_list,
                        'count': count,
                        'file': file_list
                    }

                    if tmp_list_3 in pattern_list:
                        break_sign = True
                        index_list = pattern_list.index(tmp_list_3)
                        pattern_list.pop(index_list)
                        pattern_list.append(tmp_list)
                        pattern_dict_list.pop(index_list)
                        pattern_dict_list.append(syscall_info)
                        print(syscall_info)

                    if tmp_list in pattern_list:
                        break_sign = True

                    if break_sign == False:
                        pattern_list.append(tmp_list)
                        pattern_dict_list.append(syscall_info)
                        print(syscall_info)

df1 = pd.DataFrame(pattern_list)
df2 = pd.DataFrame(pattern_dict_list)
df1.to_csv("pattern_list.csv")
df2.to_csv("pattern_dict_list.csv")
print(pattern_list)
print(pattern_dict_list)

# newdf = pd.DataFrame(index=[filename])
# for data in df['name']:
#     if data not in newdf.columns.values:
#         newdf[data] = 0
# print(newdf)
# for data in df['name']:
#     if data in newdf.columns.values:
#         newdf.loc[filename, data] = 1
# #newdf.to_csv('test.csv')
# print(newdf)
# newdf.to_csv('test.csv')
