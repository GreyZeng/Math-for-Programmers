from pathlib import Path

# 如果将单个文件和路径上的文件夹名称的字符串传递给他，Path()就会返回一个文件路径的字符串
# 包含正确的路径分隔符，在交互环境中输入以下代码
# 如果用IDEA运行这个程序，请使用 Python Console 运行
Path('spam', 'bacon', 'eggs')
# 会根据不同的操作系统返回正确的分隔符
str(Path('spam', 'bacon', 'eggs'))
myFiles = ['a.txt', 'b.txt', 'c.txt']
for file_name in myFiles:
    print(Path(r'C:\Users\zhuiz', file_name))

# WindowsPath('spam/bacon/eggs')
Path('spam') / 'bacon' / 'eggs'
# WindowsPath('spam/bacon/eggs')
Path('spam') / Path('bacon/eggs')
# 'C:\\Users\\AI\\spam'
home_folder = r'C:\Users\AI'
sub_folder = 'spam'
home_folder + '\\' + sub_folder

# 'C:\\Users\\AI\\spam'
'\\'.join([home_folder, sub_folder])
home_folder = Path('C:/Users/zhuiz')
sub_folder = Path('spam')
home_folder / sub_folder
str(home_folder / sub_folder)
Path.cwd()
str(Path.cwd())
