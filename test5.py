import os
import pandas as pd
from graphviz import Digraph
import shutil

df = pd.read_csv("G:\project\lisa_data\systemcall_selected\\0dcfa54a7e8a4e631ef466670ce604a61f3b0e8b3e9cf72c943278c0f77c31a2.out_converted.csv", index_col=0)
df = pd.read_csv("G:\project\lisa_data\systemcall_selected\\1b1a56aec5b02355b90f911cdd27a35d099690fcbeb0e0622eaea831d64014d3.out_converted.csv", index_col=0)
df = df.drop(['execname','pid'],axis=1)
column_number = df.shape[1]
row_number = df.shape[0] - 1
print(type(df.iloc[46]['arguments']))