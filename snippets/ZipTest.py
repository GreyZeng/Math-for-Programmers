import zipfile
from pathlib import Path

p = Path("C:\\eggs\\example.zip")
exampleZip = zipfile.ZipFile(p)
for name in exampleZip.namelist():
    print(name)

print(' ')
info = exampleZip.getinfo("1.txt")
print(info.file_size)
print(info.compress_size)
exampleZip.close()
