import os
import pandas as pd
import shutil

def select_system_call():
    for filename in os.listdir("G:\project\lisa_data\systemcall_all"):
        realfilename = os.path.join("G:\project\lisa_data\systemcall_all", filename)
        print(realfilename)
        df = pd.read_csv(realfilename)
        if "name" in df:
            df2 = pd.DataFrame(df["name"])
            df2.to_csv("G:\project\lisa_data\systemcall_only_name\\" + filename)

def select_empty_system_call():
    path = 'G:\project\lisa_data\systemcall_all'
    path2 = 'G:\project\lisa_data\systemcall_only_name'
    path3 = 'G:\project\lisa_data\error_systemcall'
    for filename1 in os.listdir(path):
        if filename1 not in os.listdir(path2):
            filename1_address = os.path.join(path, filename1)
            targetadress = os.path.join(path3, filename1)
            shutil.copyfile(filename1_address, targetadress)


def select_non_empty_system_call():
    path = 'G:\project\lisa_data\systemcall_all'
    path2 = 'G:\project\lisa_data\systemcall_only_name'
    path3 = 'G:\project\lisa_data\systemcall_selected'
    for filename1 in os.listdir(path):
        if filename1 in os.listdir(path2):
            filename1_address = os.path.join(path, filename1)
            targetadress = os.path.join(path3, filename1)
            shutil.copyfile(filename1_address, targetadress)

select_non_empty_system_call()
