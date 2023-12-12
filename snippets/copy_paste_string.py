import pyperclip

# 注释掉这句，然后复制一段话，可以验证
pyperclip.copy('hello,world!')
result = pyperclip.paste()
print(result)
