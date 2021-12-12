year = int(input("Введите год: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    res = ""
else:
    res = "не"

print(f"{year} год {res} является високосным")
