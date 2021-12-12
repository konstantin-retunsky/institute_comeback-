import math

print("Введите значение x")
x = float(input())
print("Введите значение α")
a = math.radians(float(input()))

y = (math.asin(math.cos(a + (math.sqrt(3) / 2) * math.pi)) + 1.2 * math.sqrt(2 - ((1 / math.tan(2 * a)) ** 2))) / (
            math.exp(0.2 * math.sqrt(x)) + 1.6 * math.log(x ** 2, 10))

res = round(y * 10 ** 3, 3)

print(f"Для x = {x} и α = {math.degrees(a)}° значение функции y = {res}")
