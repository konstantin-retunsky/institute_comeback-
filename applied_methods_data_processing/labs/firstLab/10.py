inputString = 'if2nk3el'# input().lower()
result = ""
lengthInputString = len(inputString)

for indexLetter, letter in enumerate(inputString):
    if letter.isnumeric():
        continue

    if lengthInputString != (indexLetter + 1):
        if inputString[indexLetter + 1].isnumeric():
            result += letter * int(inputString[indexLetter + 1])
        else:
            result += letter

print(result)
