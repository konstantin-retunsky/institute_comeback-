import math

inputArray = input()
arrayCalc = []
isMatrix = True

while inputArray != 'end' and isMatrix:
    inputArray = [int(item) for item in inputArray.split()]
    arrayCalc.append(inputArray)

    for item in arrayCalc:
        if len(item) != len(inputArray):
            isMatrix = False

    if isMatrix:
        inputArray = input()
    else:
        print("It's not matrix")

amountOneArray = []
amountTwo = 0

for i in range(len(arrayCalc)):
    amountOneTemp = 0

    for j in range(len(arrayCalc[0])):
        amountOneTemp += abs(arrayCalc[i][j])
        amountTwo += arrayCalc[i][j] ** 2

    amountOneArray.append(amountOneTemp)


for i in arrayCalc:
    print(i)

print(f'A2 = {max(amountOneArray)}')
print(f'A2 = {math.sqrt(amountTwo)}')
