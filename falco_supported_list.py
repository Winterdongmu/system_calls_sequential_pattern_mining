import pandas as pd
import numpy as np
import ast

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
# falco_list = falco_list_NO + falco_list_YES
# print(len(falco_list))

# print(falco_list)

df = pd.read_csv("G:\project\lisa_data\pattern_dict_list.csv", index_col=0)
sequence_list = df['sequence']
# sequence_list = np.array(df['sequence'])
# sequence_list = sequence_list.reshape(1, len(sequence_list)).tolist()
print(type(sequence_list))
new_sequence_list = []
for i in sequence_list:
    new_sequence_list.append(ast.literal_eval(i))
# print(new_sequence_list)
print(len(new_sequence_list))

good_list = []
for eachone in new_sequence_list:
    bad_mark = True
    # print(type(eachone))
    for i in eachone:
        if i not in falco_list:
            # print(i)
            bad_mark = False
    if bad_mark == True:
        good_list.append(eachone)
df1 = pd.DataFrame(good_list)
# df1.to_csv("pattern_list_filtered.csv")
print(len(good_list))