import send2trash
from pathlib import Path

# 将文件删除放入回收站
for file_name in Path("C:\\eggs").glob("*"):
    send2trash.send2trash(file_name)
