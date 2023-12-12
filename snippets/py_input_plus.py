import pyinputplus as pyip

# response = pyip.inputNum()
# response = pyip.inputInt(prompt='Enter a number: ')
# response = pyip.inputNum(prompt='Enter a number: ', min=4)
# response = pyip.inputNum(prompt='Enter a number: ', greaterThan=4)
# response = pyip.inputNum('>', min=4, lessThan=6)
# response = pyip.inputNum('>', min=4, lessThan=6)
# response = pyip.inputNum(blank=True)
# 两次输入错误就报错
# response = pyip.inputNum(limit=2)
# 10 秒等待还没输入成功就报错
# response = pyip.inputNum(timeout=10)
# 不会引发 RetryLimitException, 只会返回字符串 N/A
# response = pyip.inputNum(limit=2, default="N/A")
# response = pyip.inputNum(allowRegexes=[r"(I|V|X|L|C|D|M)+", r"zero"])
# inputNum不接收偶数作为有效输入
# response = pyip.inputNum(blockRegexes=[r"[02468]$"])
response = pyip.inputStr(
    allowRegexes=[r"caterpillar", "category"], blockRegexes=[r"cat"]
)
print(response)
