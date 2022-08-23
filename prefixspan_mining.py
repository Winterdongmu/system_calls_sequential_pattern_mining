from prefixspan import PrefixSpan

from sequential.seq2pat import Seq2Pat, Attribute
import os
import pandas as pd

path = "G:\project\lisa_data\syscall_test_1"

list_all = []
file_all = []
for filename in os.listdir(path):
    realfilename = os.path.join(path, filename)
    df = pd.read_csv(realfilename)
    list_all.append(df['name'].tolist())
    file_all.append(filename)


list_length_all = len(list_all)
pattern_list = []
pattern_dict_list = []

# df1 = pd.DataFrame(list_all)
# df1.to_csv("list_all_for_java.csv")

from spmf import Spmf
spmf = Spmf("CloFast", input_filename="test_list.txt",
            output_filename="output.txt", arguments=[0.4])
spmf.run()
print(spmf.to_pandas_dataframe(pickle=True))
spmf.to_csv("output.csv")
print(list_all)
# with open('test_list.txt','w') as f:
#     for i in list_all:
#         for j in i:
#             f.write(j)
#             f.write(' ')
#             f.write('-1')
#             f.write(' ')
#         f.write('-2')
#         f.write('\n')
#     f.close()
