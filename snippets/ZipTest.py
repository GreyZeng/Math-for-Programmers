import zipfile
from pathlib import Path


# 这个方法是解决中文文件名称乱码问题
def support_gbk(zip_file=zipfile.ZipFile):
    name_to_info = zip_file.NameToInfo
    # copy map first
    for f_name, f_info in name_to_info.copy().items():
        real_name = f_name.encode('cp437').decode('gbk')
        if real_name != f_name:
            f_info.filename = real_name
            del name_to_info[f_name]
            name_to_info[real_name] = f_info
    return zip_file


pd = Path("C:\\eggs")
# 读取压缩文件内容
p = Path(pd / "example.zip")
exampleZip = zipfile.ZipFile(p)
for name in exampleZip.namelist():
    print(name.encode('cp437').decode('gbk'))

print(' ')
info = exampleZip.getinfo("1.txt")
print(info.file_size)
print(info.compress_size)
exampleZip.close()

# 从ZIP文件中解压所有文件
exampleZip = support_gbk(zipfile.ZipFile(p))
exampleZip.extractall(pd)
exampleZip.close()

# 解压单个文件
p = Path(pd / "example2.zip")
exampleZip = support_gbk(zipfile.ZipFile(p))
exampleZip.extract('2.txt', pd)
exampleZip.close()
