import re

# 正则表达式复习
# ?匹配零次或一次前面的分组
# *匹配零次或多次前面的分组
# +匹配一次或多次前面的分组
# {n}匹配n次前面的分组
# {n,}匹配n次或更多次前面的分组
# {,m}匹配0次到m次前面的分组
# {n,m}匹配至少n次，至多m次前面的分组
# {n,m}?、*?或+?对前面的分组进行非贪心匹配
# ^spam意味着字符串必须以spam开始
# spam$意味着字符串必须以spam结束
# .匹配所有字符，换行符除外
# \d,\w和\s分别匹配数字、单词和空格
# \D,\W和\S分别匹配数字、单词和空格外的所有字符
# [abc] 匹配方括号内的任意字符(如a、b或c)
# [^abc] 匹配不在方括号内的任意字符
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4235')
print(mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4235')
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 333-3323.')

print(mo.group(1))
print(mo.group(2))

# 使用管道匹配多个分组
hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey.')
print(mo1.group())
mo1 = hero_regex.search(' Tina Fey and Batman.')
print(mo1.group())

hero_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = hero_regex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# 用问号实现可选匹配

hero_regex = re.compile(r'Bat(wo)?man')
mo = hero_regex.search('The Adventures of Batman')
print(mo.group())

mo = hero_regex.search('The Adventures of Batwoman')
print(mo.group())

phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4343')
print(mo.group())

mo = phoneNumRegex.search('My number is 444-3432')
print(mo.group())

# 用星号匹配零次或多次
hero_regex = re.compile(r'Bat(wo)*man')
print(hero_regex.search('The Adventures of Batman').group())
print(hero_regex.search('The Adventures of Batwoman').group())
print(hero_regex.search('The Adventures of Batwowowowoman').group())

# 用加号匹配一次或多次
hero_regex = re.compile(r'Bat(wo)+man')
print(hero_regex.search('The Adventures of Batwoman').group())
print(hero_regex.search('The Adventures of Batwowowowoman').group())
print(hero_regex.search('The Adventures of Batman') is None)

# 用花括号匹配特定次数

hero_regex = re.compile(r'(ha){3}')
print(hero_regex.search('hahaha').group())
print(hero_regex.search('ha') is None)

# 贪心和非贪心匹配
# 默认是贪心的，所以下述正则会匹配到最长的那个字符串
greedy_ha_regex = re.compile(r'(Ha){3,5}')
mo = greedy_ha_regex.search('HaHaHaHaHa')
print(mo.group())
# 加了一个问好，则变成非贪心的，所以下述正则会匹配到最短的那个字符串
greedy_ha_regex = re.compile(r'(Ha){3,5}?')
mo = greedy_ha_regex.search('HaHaHaHaHa')
print(mo.group())

# findAll 方法 找到所有匹配的字符串
# 如果在一个没有分组的正则表达式上调用，例如下述情况
# findAll方法将返回一个匹配字符串的列表
phone_reg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_reg.findall('Cell: 453-432-5555 Work: 453-908-8887')
print(mo)
# 如果在一个有分组的正则表达式上调用，例如下述情况
# findAll方法将返回一个字符串的元组的列表
phone_reg = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phone_reg.findall('Cell: 453-432-5555 Work: 453-908-8887')
print(mo)

# 字符分类

# \d : 0 ~ 9 的任何数字
# \D : 除 0 ~ 9 的数字以外的任何字符
# \w : 任何字符、数字或下划线字符（可以认为是匹配“单词”字符）
# \W : 除字母、数字和下划线以外的任何字符
# \s : 空格、制表符或换行符（可以认为是匹配空白字符）
# \S : 除空格、制表符和换行符以外的任何字符
xmas_regex = re.compile(r'\d+\s\w+')
print(xmas_regex.findall('12 abc, 23 bbb, d 44 ,34    abc, 44 444, 33 abc'))
# 匹配元音字符
reg = re.compile(r'[aeiouAEIOU]')
print(reg.findall('I love you'))
# 在字符分类的左方括号后加入一个插入字符(^), 就可以得到“非字符类”，
# 例如下面例子，就是匹配非元音字符
reg = re.compile(r'[^aeiouAEIOU]')
print(reg.findall('I love you'))

# 在正则表达式的开始处使用插入符号（^), 表明匹配必须发生在被查找文本的开始处
reg = re.compile(r'^hello')
print(reg.search('hello world!'))
print(reg.search('world hello') is None)

# 正则表达式 r'\d$' 匹配以数字 0 ~ 9 结束的字符串。
reg = re.compile(r'\d$')
print(reg.search('Your number is 999'))
print(reg.findall('Your number is 999'))
# r'\d+$' 匹配从开始到结束都是数字的字符串。
reg = re.compile(r'^\d+$')
print(reg.search("12334545"))
print(reg.search("12334x545") is None)
print(reg.search("1233  545") is None)
# .字符称为“通配字符”，它匹配换行符以外的所有字符
reg = re.compile(r'.at')
print(reg.findall('The cat in the hat sat on the flat mat.'))
# .* 表示任意文本(贪心模式）：点表示换行符外的所有单个字符，星号表示前面字符出现0次或多次
reg = re.compile(r'First Name:(.*) Last Name:(.*)')
print(reg.search("First Name:Grey Last Name:Zeng").group(1))
print(reg.search("First Name:Grey Last Name:Zeng").group(2))
# 如果要改成非贪心模式，需要加上问号
reg = re.compile(r'<.*?>')
# 输出：<To serve man>
print(reg.search('<To serve man> for dinner.>').group())
reg = re.compile(r'<.*>')
# 输出：<To serve man> for dinner.>
print(reg.search('<To serve man> for dinner.>').group())
# .*如果要匹配包括换行符的所有字符，可以加一个参数
reg = re.compile('.*', re.DOTALL)
print(reg.search("abc \n cdef\n aaa"))
# 不区分大小写的匹配，增加一个配置参数
reg = re.compile(r'robot', re.I)
print(reg.findall("robot  RobOT  rOBot roboT"))
# sub()方法第一个参数是一个字符串，用户替换发现的匹配。第二个参数是一个字符串，即正则表达式，方法返回替换完成后的字符串
reg = re.compile(r'Agent \w+')
print(reg.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
