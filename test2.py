listc = [1, 2, 3]
liste = [1, 2, 3, 4]
lista = [1, 2, 3, 4, 5]
listb = [1, 2, 3, 4, 5, 6, 7]
list1 = [1,2,6,7]
list2 = ["5","2","1"]
list3 = ["2", "1", "7","5"]
list_all = [listc, liste, lista, listb]


print(list(set(list2)&set(list3)))



# pattern = []
# for i in list_all:
#     for j in range(len(i)):
#         i_tmp = i[:]
#
#         i_tmp.pop(j)
#         print(i_tmp)
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
#         print(pattern)
# # print(pattern)
