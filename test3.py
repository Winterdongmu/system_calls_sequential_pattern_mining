import os
import pandas as pd
import operator
path = "G:\project\lisa_data\syscall_test_1"






list_all = []


for filename in os.listdir(path):
    realfilename = os.path.join(path, filename)
    #print(realfilename)
    df = pd.read_csv(realfilename)
    list_all.append(df['name'].tolist())
#print(list_all[0])

list_length_all = len(list_all)



threshold = 8
compare_value = 8
pattern_list = []

for first_index in range(0, list_length_all):
    print("\n")
    print("first_index:",first_index)
    first_list_length_single = len(list_all[first_index])
    for first_list_index in range(0, first_list_length_single-threshold):
        tmp_list = []
        for i in range (0,threshold):
            tmp_list.append(list_all[first_index][first_list_index+i])
        if tmp_list not in pattern_list:
            count = 0
            for second_index in range(0, list_length_all):
                # print("second_index:",second_index,"(",first_index,")")
                if first_index != second_index:
                    second_list_length_single = len(list_all[second_index])
                    for second_list_index in range(0,second_list_length_single-threshold):
                        tmp_list_2 = []
                        for i in range(0, threshold):
                            tmp_list_2.append(list_all[second_index][second_list_index + i])

                        if operator.eq(tmp_list,tmp_list_2):
                            print(tmp_list)
                            print(tmp_list_2)
                            print(operator.eq(tmp_list, tmp_list_2))
                            print(first_index)
                            print(second_index)
                            count += 1
            if count >= compare_value:
                pattern_list.append(tmp_list)

print(pattern_list)




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
