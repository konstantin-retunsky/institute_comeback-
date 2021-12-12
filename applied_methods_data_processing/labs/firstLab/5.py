inputNumber = int(input("Введите число:"))
start = int(input("Введите начало отрезка:"))
end = int(input("Введите конец отрезка:"))

resultFor = []
resultWhile = []
for i in range(start, end + 1):
    if i % inputNumber == 0:
        resultFor.append(i)

i = start
while i <= end:
    i += 1
    if i % inputNumber == 0:
        resultWhile.append(i)

if len(resultFor) == 0:
    print(
        "В отрезке нет кратных чисел")

else:
    print(sum(resultFor) / len(resultFor))
