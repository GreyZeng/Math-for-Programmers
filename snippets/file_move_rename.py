import shutil

# bacon.txt文件移动到eggs文件夹
shutil.move("C:\\bacon.txt", 'C:\\eggs')
# 移动并重命名
shutil.move("C:\\meat.txt", 'C:\\eggs\\meat_bak.txt')
