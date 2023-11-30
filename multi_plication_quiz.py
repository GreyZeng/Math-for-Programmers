import pyinputplus as pyip
import random, time

number_of_question = 10
correct_answer = 0

for q_num in range(number_of_question):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = "#%s:%s x %s = " % (q_num, num1, num2)
    try:
        pyip.inputStr(
            prompt,
            allowRegexes=["^%s$" % (num1 * num2)],
            blockRegexes=[(".*", "Incorrect!")],
            timeout=8,
            limit=3,
        )
    except pyip.TimeoutException:
        print("Out of time!")
    except pyip.RetryLimitException:
        print("Out of tries!")
    else:
        print("correct!")
