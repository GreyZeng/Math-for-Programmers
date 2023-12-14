import os

from pathlib import Path

# unlink(path) 将删除 path 处的文件
# rmdir(path) 将删除 path 处的文件夹，该文件夹必须为空，不能有任何文件和文件夹
# rmtree(path) 删除 path 处的文件夹
for filename in Path("C:\\eggs").glob("*.txt"):
    os.unlink(filename)
