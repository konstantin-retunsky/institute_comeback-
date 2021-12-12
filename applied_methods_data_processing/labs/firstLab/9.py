inputString = 'iffnkkkel'  # input().lower()
result = ""
lastLetter = inputString[0]
countDuplicate = 0
lengthInputString = len(inputString)

for indexLetter, letter in enumerate(inputString):
    if letter == lastLetter:
        countDuplicate += 1
    else:
        if countDuplicate == 1:
            result += f'{lastLetter}'
        else:
            result += f'{lastLetter}{countDuplicate}'

        countDuplicate = 1

    lastLetter = letter

    if (indexLetter + 1) == lengthInputString:
        result += f'{lastLetter}'

print(result)
