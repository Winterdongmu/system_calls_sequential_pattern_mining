import pandas as pd
import os


def convert_to_list(behav_file):
    started = False
    syscalls = []
    with open(behav_file) as f:
        line = f.readline()
        while line:
            if line.startswith('SYSCALL'):
                syscall = {
                    'execname': f.readline()[:-1],
                    'name': f.readline()[:-1],
                    'pid': int(f.readline()[:-1]),
                    'arguments': f.readline()[:-1],
                    'return': f.readline()[:-1]
                }
                if started:
                    syscalls.append(syscall)
                else:
                    started = True
            line = f.readline()
    print(syscalls)
    df = pd.DataFrame(syscalls)
    df.to_csv(behav_file + '_' + 'converted.csv')
    # print(type(syscalls))
    # print(syscalls)


# for filename in os.listdir("G:\project\lisa_data\logs_backup_2"):
#     realfilename = os.path.join("G:\project\lisa_data\logs_backup_2", filename)
#     convert_to_list(realfilename)

def select_openfile(behav_file):
    files = []
    with open(behav_file) as f:
        line = f.readline()
        while line:

            if line.startswith('OPENFILE'):
                inner = f.readline()
                if not inner:
                    break

                file = inner.strip('"\n')
                files.append(file)

            line = f.readline()
    print(files)
    df = pd.DataFrame(files)
    df.to_csv(behav_file + '_' + 'files.csv')
    print(df)

for filename in os.listdir("G:\project\lisa_data\logs_backup_2"):
    realfilename = os.path.join("G:\project\lisa_data\logs_backup_2", filename)
    select_openfile(realfilename)