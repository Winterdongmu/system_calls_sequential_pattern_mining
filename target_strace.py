import json
import ast
import pandas as pd
import copy

falco_list_YES = ["syscall","open", "socket" ,"bind","connect", "listen", "sendto", "recvfrom", "socketpair", "setsockopt",
              "sendmsg" ,"recvmsg", "creat", "pipe","chdir", "fchdir","mkdir", "rmdir","dup","signalfd","kill","tkill","tgkill","inotify_init",
              "prlimit","ptrace","ioctl","rename","renameat","symlink","symlinkat","procexit","quotactl","setresuid","setresgid","setuid"
              ,"setgid","clone","fork","vfork","execve","setns","flock","accept","mount","umount","chroot","tracer","container"
              ,"setsid","mkdir","rmdir","unshare","execve","setpgid","bpf","seccomp","unlink","unlinkat","mkdirat","openat"
              ,"link","linkat","fchmodat","chmod","fchmod","renameat2","userfaultfd","pluginevent","container","openat2",
              "execveat","copy_file_range","clone3","open_by_handle_at","capset","useradded","groupadded","dup2","dup3","dup"]
def convert_trace():
    path = "G:\project\lisa_data\strace_frontend.log"
    empty_data = []
    with open(path) as f:
        line = f.readline()
        while line:
            if not (line.strip().endswith('+++') or line.strip().endswith('<detached ...>')):
                print(type(line))
                print(line)

                first_part,return_value = line.strip().rsplit("=",1)
                return_value = return_value.strip()
                # numbers_value, second_part = first_part.strip().split(" ",1)
                syscall_value,third_part = first_part.strip().split("(",1)
                attribute_value,empty= third_part.strip().rsplit(")",1)
                print(syscall_value)
                print(attribute_value)
                print(return_value)
                print("\n")
                syscall = {
                    'name': syscall_value,
                    'arguments': attribute_value,
                    'return': return_value
                }
                empty_data.append(syscall)
                line = f.readline()
            else:
                line = f.readline()
    df = pd.DataFrame(empty_data)
    df.to_csv('strace_logs_frontend.csv')

df = pd.read_csv("G:\project\lisa_data\signature_based_on_seq2pat.csv", index_col=0)
df2 = pd.read_csv("G:\project\lisa_data\strace_logs_frontend.csv", index_col=0)
sequence_list = df['sequence']
sequence_list2 = df['file']
new_sequence_list = []
for i in sequence_list:
    new_sequence_list.append(ast.literal_eval(i))
strace_logs = df2['name'].tolist()

print(len(new_sequence_list))
sequence_white = []
for i in new_sequence_list:
    tmp_length = len(i)
    if set(i).issubset(set(strace_logs)):
        pos_list = [k for k, x in enumerate(strace_logs) if x == i[0]]
        for index in pos_list:
            if strace_logs[index:index + tmp_length] == i and (index + tmp_length) <= len(strace_logs):
                sequence_white.append(i)
                break

print(sequence_white)
print(len(sequence_white))
for i in sequence_white:
    new_sequence_list.remove(i)
print(len(new_sequence_list))

new_sequence_list_backup = copy.deepcopy(new_sequence_list)
for i in new_sequence_list:
    for j in i:
        if j not in falco_list_YES:

            new_sequence_list_backup.remove(i)
            break

print(new_sequence_list_backup)
print(len(new_sequence_list_backup))
print(new_sequence_list_backup.index(['openat', 'openat', 'openat', 'openat']))

for i in new_sequence_list_backup[5]:
    text ="- rule: "+i+"\n"+"  desc: "+i+"\n"+"  condition: container.id in (target_container) and evt.type = "+i+"\n"+"  output: "+ "\""+"Systemcall: "+i+"(user=%user.name %container.info parent=%proc.pname cmdline=%proc.cmdline)"+"\""+"\n"+"  priority: ERROR" + "\n" +"  tags: [users, container]" + "\n"
    print(text)

df3  = pd.DataFrame(new_sequence_list)
df3.to_csv("whilte_list_filter.csv")
df4 = pd.DataFrame(new_sequence_list_backup)
df4.to_csv("whilte_list_filter_YES.csv")


