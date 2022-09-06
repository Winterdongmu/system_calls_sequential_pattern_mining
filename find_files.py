import copy

import pandas as pd
import numpy as np
import ast
import os
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
# df = pd.read_csv("G:\project\lisa_data\Simplified_pattern_dictionary.csv", index_col=0)
df2 = pd.read_csv("G:\project\lisa_data\seq2pat_pattern_list_plus.csv", index_col=0)
path = "G:\project\lisa_data\syscall_test_2"

list_all = []
file_all = []
for filename in os.listdir(path):
    realfilename = os.path.join(path, filename)
    # print(realfilename)
    df = pd.read_csv(realfilename)
    list_all.append(df['name'].tolist())
    file_all.append(filename)


itemset = df2.values.tolist()
for i in itemset:
    while np.nan in i:
        i.remove(np.nan)
        # i.pop()

good_list = []
print(len(itemset))
for eachone in range(len(itemset)):
    bad_mark = True
    # print(type(eachone))
    for i in itemset[eachone]:
        if i not in falco_list:
            # print(i)
            bad_mark = False
    if bad_mark == True:
        good_list.append(itemset[eachone])

# set(test_list_3).issubset(set(test_list_1))
# tmp_length = len(test_list_2)
# pos_list = [i for i, x in enumerate(test_list_1) if x == test_list_2[0]]
# print(test_list_1[pos_list[1]:pos_list[1]+tmp_length])
signature_dict_list = []
for i in good_list:
    tmp_file_list = []
    for j in range(len(list_all)):
        if set(i).issubset(set(list_all[j])):
            tmp_length = len(i)
            pos_list = [k for k, x in enumerate(list_all[j]) if x == i[0]]
            for index in pos_list:
                if list_all[j][index:index+tmp_length] == i and (index+tmp_length) <= len(list_all[j]):
                    tmp_file_list.append(file_all[j])
                    break
    signature_info = {
        'sequence': i,
        'file': tmp_file_list
    }
    signature_dict_list.append(signature_info)

df4 = pd.DataFrame(signature_dict_list)
df4.to_csv("signature_based_on_seq2pat_test.csv")

for i in range(len(signature_dict_list)):
    for j in range(i+1,len(signature_dict_list)):
        if set(signature_dict_list[i]['sequence']).issubset(set(signature_dict_list[j]['sequence'])):
            tmp_length = len(signature_dict_list[i]['sequence'])
            pos_list = [k for k, x in enumerate(signature_dict_list[j]['sequence']) if x == signature_dict_list[i]['sequence'][0]]
            for index in pos_list:
                if signature_dict_list[j]['sequence'][index:index + tmp_length] == signature_dict_list[i]['sequence'] and (index + tmp_length) <= len(signature_dict_list[j]['sequence']):
                    intersection_list = []
                    intersection_list = list(set(signature_dict_list[i]['file']).intersection(signature_dict_list[j]['file']))
                    for value in intersection_list:
                        signature_dict_list[i]['file'].remove(value)
                    break


signature_dict_list_back_up = copy.deepcopy(signature_dict_list)
for i in range(len(signature_dict_list)):
    if not signature_dict_list[i]['file']:
        for k in range(len(signature_dict_list_back_up)):
            if signature_dict_list[i]['sequence'] == signature_dict_list_back_up[k]['sequence']:
                signature_dict_list_back_up.pop(k)
                break



df3 = pd.DataFrame(signature_dict_list_back_up)
df3.to_csv("signature_based_on_seq2pat.csv")
print(signature_dict_list)



