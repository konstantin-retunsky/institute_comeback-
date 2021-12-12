from unittest import result

numberOne = int(input("Введите число 1:"))
operation = input("Введите одну из следующих операций: +, -, *, /, //, %, **")
numberTwo = int(input("Введите число 2:"))

if operation.lower() == "+":
    result = numberOne + numberTwo
elif operation.lower() == "-":
    result = numberOne - numberTwo
elif operation.lower() == "*":
    result = numberOne * numberTwo
elif operation.lower() == "/" and numberTwo != 0:
    result = numberOne / numberTwo
elif operation.lower() == "//" and numberTwo != 0:
    result = numberOne // numberTwo
elif operation.lower() == "%" and numberTwo != 0:
    result = numberOne % numberTwo
elif operation.lower() == "**" and not (numberOne == 0 and numberTwo < 0):
    result = numberOne ** numberTwo
else:
    if numberTwo == 0:
        result = 'На ноль делить нельзя'
    elif numberOne == 0 and numberTwo < 0:
        result = 'Ноль не может быть возведина в отрицательную степень'
    else:
        result = "Операция невозможна"

print(result)
