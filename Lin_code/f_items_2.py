import os,sys,csv
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

import pandas as pd
import numpy as np
import ast
import copy
from sequential.seq2pat import Seq2Pat, Attribute
falco_list_YES = ["syscall","open", "socket" ,"bind","connect", "listen", "sendto", "recvfrom", "socketpair", "setsockopt",
              "sendmsg" ,"recvmsg", "creat", "pipe","chdir", "fchdir","mkdir", "rmdir","dup","signalfd","kill","tkill","tgkill","inotify_init",
              "prlimit","ptrace","ioctl","rename","renameat","symlink","symlinkat","procexit","quotactl","setresuid","setresgid","setuid"
              ,"setgid","clone","fork","vfork","execve","setns","flock","accept","mount","umount","chroot","tracer","container"
              ,"setsid","mkdir","rmdir","unshare","execve","setpgid","bpf","seccomp","unlink","unlinkat","mkdirat","openat"
              ,"link","linkat","fchmodat","chmod","fchmod","renameat2","userfaultfd","pluginevent","container","openat2",
              "execveat","copy_file_range","clone3","open_by_handle_at","capset","useradded","groupadded","dup2","dup3","dup"]
falco_list_NO = [
    "close", "read", "write","send","recv","shutdown","getsockname","getpeername","getsockopt","sendmmsg","recvmmsg","eventfd",
    "futex","stat","lstat","fstat","stat64","lstat64","fstat64","epoll_wait","poll","select","lseek","llseek","getcwd","pread",
    "pwrite","readv","writev","preadv","pwritev","nanosleep","timerfd_create","getrlimit","setrlimit","fcntl","switch","brk","mmap",
    "mmap2","munmap","splice","sendfile","getuid","geteuid","getgid","getegid","getresuid","getresgid","signaldeliver","getdents","getdents64",
    "cpu_hotplug","semop","semctl","ppoll","semget","access","notification","page_fault","mprotect","io_uring_setup","io_uring_enter",
    "io_uring_register","mlock","munlock","mlockall","munlockall"
]


falco_list = list(set(falco_list_NO + falco_list_YES))
df = pd.read_csv("G:\project\lisa_data\Simplified_pattern_dictionary.csv", index_col=0)
sequence_list = df['sequence']
file_list = df['file']
# sequence_list = np.array(df['sequence'])
# sequence_list = sequence_list.reshape(1, len(sequence_list)).tolist()
# print(sequence_list)
# print(file_list)

new_sequence_list = []
for i in sequence_list:
    print(i)
    new_sequence_list.append(ast.literal_eval(i))
new_file_list = []
for i in file_list:
    new_file_list.append(list(set(ast.literal_eval(i))))
# print(new_file_list)

good_list = []

for eachone in range(len(new_sequence_list)):
    bad_mark = True
    # print(type(eachone))
    for i in new_sequence_list[eachone]:
        if i not in falco_list:
            # print(i)
            bad_mark = False
    if bad_mark == True:
        good_list.append(new_file_list[eachone])


tr = TransactionEncoder()
tr_arr = tr.fit(good_list).transform(good_list)
df = pd.DataFrame(tr_arr, columns=tr.columns_)
#print(df)
frequent_itemsets = apriori(df, min_support = 0.04, use_colnames = True) # 2%-13%: 0.1, 1%
#frequent_itemsets = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# print(frequent_itemsets["itemsets"])

# frequent_itemsets.to_csv("frequent_itemsets_apriori.csv")
original_list = []
support_list = []
for item in frequent_itemsets["itemsets"]:
    original_list.append(list(item))
for item in frequent_itemsets["support"]:
    support_list.append(item)
print(len(support_list))
print(len(original_list))

# newlist = list(reversed(original_list))

pattern = []
for i in original_list:
    for j in range(len(i)):
        i_tmp = i[:]

        i_tmp.pop(j)
        # print(i_tmp)
        if i_tmp in pattern and i in pattern:
            index = pattern.index(i_tmp)
            pattern.pop(index)
            # pattern.append(i)
        elif i_tmp in pattern and i not in pattern:
            index = pattern.index(i_tmp)
            pattern.pop(index)
            pattern.append(i)
        elif i not in pattern:
            # print(i)
            pattern.append(i)

print(len(pattern))


df2 = pd.DataFrame(pattern)
df2.to_csv("frequent_itemsets_apriori_filtered.csv")

