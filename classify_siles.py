import pandas as pd
path = "G:\project\lisa_data\systemcall_files\\0a79399c441fca30d20e79fdabdd23ae33f3e16bf9c012cd1492604a03e656bb" \
       ".out_files.csv "
path2 = "G:\project\lisa_data\collect_files.csv"

df_target = pd.read_csv(path2, index_col=0)

row_number = list(range(len(df_target)))
row_number2 = list(range(len(df_target)))
row_number2.pop()

share_dictionary = {}
specific_files_dict = {}
colume_name = df_target.columns.values

for i in row_number2:
       file_count = 0
       first_list = []

       share_file_store = []

       share_file_store_index = 0

       first_target = df_target.iloc[[i]]

       for colume_index in colume_name:
              if first_target[colume_index].iloc[0] == 1:
                     file_count += 1

       row_number.pop(0)
       for ii in row_number:
              share_count = 0
              share_file_store_tmp = []
              second_target = df_target.iloc[[ii]]
              second_file_count = 0
              for colume_index in colume_name:
                     if second_target[colume_index].iloc[0] == 1:
                            second_file_count += 1

              for colume_index in colume_name:
                     if first_target[colume_index].iloc[0] == 1 and first_target[colume_index].iloc[0] == second_target[colume_index].iloc[0]:
                            share_count += 1
                            share_file_store_tmp.append(colume_index)

              if share_count/file_count >= 0.7 and second_file_count/file_count < 2:
                     first_list.append(second_target._stat_axis.values.tolist()[0])
                     df_target.drop(df_target.index[ii], inplace=True)
                     share_file_store.append([])
                     share_file_store[share_file_store_index] = share_file_store_tmp
                     # print(share_file_store)
                     # print('\n')
                     share_file_store_index += 1


                     row_number.pop()
                     row_number2.pop()
                     # print(df_target.index[ii])
                     # print(row_number)
                     # print('\n')
       share = []
       if len(share_file_store) != 0:
              share = share_file_store[0]
              for i in range(len(share_file_store)):
                     share = set(share) & set(share_file_store[i])
       print(share)
       share_dictionary[first_target._stat_axis.values.tolist()[0]] = first_list
       specific_files_dict[first_target._stat_axis.values.tolist()[0]] = share
# print(share_dictionary)
#pd.DataFrame(share_dictionary).to_csv('classify_based_on_files.csv')
df = pd.DataFrame.from_dict(share_dictionary, orient='index')
df.T.to_csv('classify_based_on_files.csv')
print(specific_files_dict)
df2 = pd.DataFrame.from_dict(specific_files_dict, orient='index')
df2.T.to_csv('classify_based_on_files_specific.csv')
# print(df.T)


# print(len(df_target))
# # print(df_target.iloc[0])
# # print(df_target.iloc[0:2])
# print(df_target.iloc[[1]])