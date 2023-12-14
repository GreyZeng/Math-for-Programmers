import shutil
from pathlib import Path

p = Path.home()
# 将 spam.txt 复制到 some_folder 文件夹下
shutil.copy(p / 'spam.txt', p / 'some_folder')
