# 遍历目录树
import os
from pathlib import Path

for folder_name, sub_folders, file_names in os.walk(Path.home()):
    print('The Current folder is ' + folder_name)
    for sub_folder in sub_folders:
        print('SUBFOLDER OF ' + folder_name + ": " + sub_folder)
    for file_name in file_names:
        print('FILE INSIDE ' + folder_name + ": " + file_name)
    print(' ')
