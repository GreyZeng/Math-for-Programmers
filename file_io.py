from pathlib import Path

# 如果将单个文件和路径上的文件夹名称的字符串传递给他，Path()就会返回一个文件路径的字符串
# 包含正确的路径分隔符，在交互环境中输入以下代码

path = Path("a", "b", "c")
print(path)
print(str(Path("a", "b", "c")))

myFiles = ["a.txt", "b.txt", "c.txt"]
for file_name in myFiles:
    print(Path(r"C:\workspace", file_name))
