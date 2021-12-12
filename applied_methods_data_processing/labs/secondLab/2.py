import numpy as np
from matplotlib import pyplot as plt

inputX = 23  # float(input('input x: '))

funcOne = 2 * np.sin(inputX ** 2) + np.cos(inputX ** 2)

plt.plot(1, 3, '-o')
plt.show()
