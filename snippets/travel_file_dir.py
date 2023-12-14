# 遍历目录树
import os
from pathlib import Path

# os.walk 返回三个值
# 当前文件夹名称的字符串
# 当前文件夹中子文件夹的字符串的列表
# 当前文件夹中文件的字符串列表
for folder_name, sub_folders, file_names in os.walk(Path.home()):
    print('The Current folder is ' + folder_name)
    for sub_folder in sub_folders:
        print('SUB FOLDER OF ' + folder_name + ": " + sub_folder)
    for file_name in file_names:
        print('FILE INSIDE ' + folder_name + ": " + file_name)
    print(' ')
