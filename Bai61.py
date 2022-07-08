import numpy as np
import matplotlib.pyplot as plt
x = np.array([10, 23, 56 , 13 , 56, 24, 64, 56, 35,37])
y = np.array([1, 2,3,4, 5,6, 7,8, 9,12])
plt.subplot(1, 2, 1)
plt.plot(x,y)
x = np.arange(-10, 10)
y = 3*x**3 - 3*x*x + 3*x - 3
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.show()