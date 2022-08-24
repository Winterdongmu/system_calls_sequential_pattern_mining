listc = [1,2,3]
liste = [1,2,3,4]
lista = [1,2,3,4,5]
listb = [1,2,3,4,5,6,7]
list_all = [listc,liste,lista,listb]
list_signature = [['sched_setaffinity', 'sched_setaffinity'], ['pipe2', 'write'], ['sched_getaffinity', 'sched_setaffinity', 'sched_setaffinity'], ['eventfd2', 'rt_sigprocmask', 'read'], ['write', 'rt_sigprocmask', 'rt_sigaction'], ['sched_getaffinity', 'sched_getaffinity', 'sched_setaffinity', 'sched_setaffinity'], ['pipe2', 'eventfd2', 'rt_sigprocmask', 'read'], ['rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['close', 'sched_getaffinity', 'sched_getaffinity', 'sched_setaffinity', 'sched_setaffinity'], ['read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigprocmask', 'read', 'rt_sigaction', 'write', 'rt_sigprocmask', 'rt_sigaction'], ['openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat'], ['openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read'], ['openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close'], ['read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat'], ['close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read'], ['close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat'], ['openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat'], ['read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat'], ['close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat'], ['openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat'], ['read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat'], ['close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read'], ['openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close'], ['read', 'close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat'], ['close', 'openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read'], ['openat', 'read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close'], ['read', 'close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat'], ['close', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read'], ['openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close'], ['openat', 'openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat'], ['openat', 'openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read'], ['openat', 'openat', 'openat', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close', 'openat', 'read', 'close']]
pattern = []
dict1 = {"a":1,"b":2,"c":3}
if "a" in dict1:
    dict1["a"] += 1
print(dict1["a"])







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