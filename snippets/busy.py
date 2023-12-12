import pyinputplus as pyip

# while True:
#     prompt = "Want to know how to keep a person busy for hours?\n"
#     response = pyip.inputYesNo(prompt)
#     if response == 'no':
#         break
#
# print('Thank you , have a nice day.')
while True:
    prompt = "Want to know how to keep a person busy for hours?\n"
    response = pyip.inputYesNo(prompt, yesVal="y", noVal="n")
    if response == "n":
        break

print("Thank you , have a nice day.")
