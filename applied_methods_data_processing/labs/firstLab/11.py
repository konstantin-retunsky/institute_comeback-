import math
from scipy.spatial import distance

inputFirstVectors = [3, 3, 3]  # [int(item) for item in input().split()]
inputSecondVectors = [1, 2, 3]  # [int(item) for item in input().split()]
result = 0.0

if len(inputFirstVectors) != len(inputSecondVectors):
    print("Количество элементов не совпадает")

for index in range(len(inputSecondVectors)):
    result += (inputFirstVectors[index] - inputSecondVectors[index]) ** 2

print(math.sqrt(result))

print(distance.euclidean(inputFirstVectors, inputSecondVectors))