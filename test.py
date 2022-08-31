listc = [1,2,3]
liste = [1,2,3,4]
lista = [1,2,3,4,5]
listb = [1,2,3,4,5,6,7]
list_all = [listc,liste,lista,listb]
list_signature = [['sched_setaffinity', 'sched_setaffinity'], ['pipe2', 'write'], ['sched_getaffinity', 'sched_setaffinity', 'sched_setaffinity'], ['eventfd2', 'rt_sigprocmask', 'read'], ['write', 'rt_sigprocmask', 'rt_sigaction'], ['sched_getaffinity', 'sched_getaffinity', 'sched_setaffinity', 'sched_setaffinity'], ['pipe2', 'eventfd2', 'rt_sigprocmask', 'read'], ['rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['close', 'sched_getaffinity', 'sched_getaffinity', 'sched_setaffinity', 'sched_setaffinity'], ['read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat'], ['openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read'], ['openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close'], ['read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat'], ['close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read'], ['close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat'], ['openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat'], ['read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat'], ['close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat'], ['openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat'], ['read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat'], ['close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read'], ['openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close'], ['read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat'], ['close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read'], ['openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close'], ['read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat'], ['close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read'], ['openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close'], ['openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat'], ['openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read'], ['openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close']]
pattern = []
dict1 = {"a":1,"b":2,"c":3}
test_list_1 = ['getppid', 'uname', 'stat', 'stat', 'rt_sigaction', 'rt_sigaction', 'rt_sigaction']
test_list_2 = ['stat', 'rt_sigaction']
test_list_3 = ['rt_sigaction', 'stat']
test_list_4 = [['stat', 'rt_sigaction'],['rt_sigaction', 'stat'],['getppid', 'uname', 'stat', 'stat', 'rt_sigaction', 'rt_sigaction', 'rt_sigaction']]
test_list_5 = ['stat', 'rt_sigaction']

print(set(test_list_2).issubset(set(test_list_5)))
# if "a" in dict1:
#     dict1["a"] += 1
# print(dict1["a"])
# set(test_list_3).issubset(set(test_list_1))
# tmp_length = len(test_list_2)
# pos_list = [i for i, x in enumerate(test_list_1) if x == test_list_2[0]]
# # print(test_list_1[pos_list[1]:pos_list[1]+tmp_length])
#
#
# print(set(test_list_1))
# print(test_list_1)
#
# if test_list_2 in test_list_1:
#     print(1)
# import pandas as pd
# import ast
# df = pd.read_csv("G:\project\lisa_data\Simplified_pattern_dictionary.csv", index_col=0)
# sequence_list = df['sequence']
# file_list = df['file']
#
# print(sequence_list)




# sequence_list = np.array(df['sequence'])
# sequence_list = sequence_list.reshape(1, len(sequence_list)).tolist()
# print(sequence_list)
# print(file_list)

# new_sequence_list = []
# for i in sequence_list:
#     # print(i)
#     new_sequence_list.append(ast.literal_eval(i))
# max_length = len(new_sequence_list[0])
# for i in new_sequence_list:
#     if len(i) > max_length:
#         max_length = len(i)
#         print(i)
#         # print(len(i))
# print(max_length)
# list_new = list(reversed(list_all))
# print(list_new)



# for i in list_all:
#     i_tmp = i[:]
#     i_tmp.pop()
#     # print(i_tmp)
#     # print(i)
#     # print('\n')
#     if i_tmp in pattern:
#         index = pattern.index(i_tmp)
#         pattern.pop(index)
#         pattern.append(i)
#     else:
#         pattern.append(i)
# print(pattern)
# print(list_all)
# newlist = list(reversed(list_all))
# print(newlist)