import math

x = 2
k = 0
a = 1

result = 0.0

while abs(a) > 10**-5:
    k += 1
    result += a
    a = (x ** k) / (math.factorial(k))

print(result, "it's calculate")
print(math.exp(x), "it's lib exp")
