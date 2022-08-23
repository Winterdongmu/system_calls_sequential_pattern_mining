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


def collect_system_calls():

    for filename in os.listdir("G:\project\lisa_data\systemcall_selected"):
        realfilename = os.path.join("G:\project\lisa_data\systemcall_selected", filename)
        print(realfilename)
        df = pd.read_csv(realfilename)
        newdf = pd.DataFrame(index=[filename])
        for data in df['name']:
            if data not in newdf.columns.values:
                newdf[data] = 0
        print(newdf)
        for data in df['name']:
            if data in newdf.columns.values:
                newdf.loc[filename, data] = 1
        #newdf.to_csv('test.csv')
        print(newdf)
    newdf.to_csv('test.csv')

collect_system_calls()