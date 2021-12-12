import numpy as np


def func(t):
    return np.sin(t / 2) * np.exp(-(t / 4)) + 2 * np.exp(-(t / 2))


inputVector = np.array([1, 2, 3, 4])  # np.array([int(i) for i in input().split('Input vector: ')])
inputNumber = 13  # int(input().split('Input number: '))

print(func(inputVector))
print(func(inputNumber))
