import os
import shutil


path = '/home/lin/Documents/Lisa/lisa/data/storage'
count = 0
for filename in os.listdir(path):
    folder_name = os.path.join(path,filename)
    if os.path.isdir(folder_name) and os.path.isfile(os.path.join(folder_name,'behav.out')):
        for file in os.listdir(folder_name):
            if len(file) > 20:
                newfilename = os.path.join('/home/lin/Documents/logs_backup_2',file)+'.out'
                file_path = os.path.join(folder_name,'behav.out')
                shutil.copyfile(file_path, newfilename)
                # newfilename = os.path.join(folder_name, file)
                # os.remove(newfilename)



