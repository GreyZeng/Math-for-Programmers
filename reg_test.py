import re

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
print(hero_regex.search('The Adventures of Batman') == None)

# 用花括号匹配特定次数

hero_regex = re.compile(r'(ha){3}')
print(hero_regex.search('hahaha').group())
print(hero_regex.search('ha') == None)