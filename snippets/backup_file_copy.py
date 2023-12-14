import shutil
from pathlib import Path

p = Path.home()
# 备份所有 spam文件夹里面的内容
shutil.copytree(p / 'spam', p / 'spam_backup')
