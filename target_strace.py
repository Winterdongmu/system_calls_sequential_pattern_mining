import json
import ast
import pandas as pd
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

