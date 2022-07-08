import numpy as np
import matplotlib.pyplot as plt
import math
x = np.linspace(-10, 10)
y = np.sin(x)
font = {"family": "consolas", "color":"blue", "size":14}
plt.grid(axis="y")
plt.title("Đồ thị Y= SIN(X)")
plt.xlabel("Trục X", loc = "right", fontdict=font)
plt.ylabel("Trục Y", loc= "top", fontdict=font)
plt.plot(x, y, marker = "*", ms = 12, mec= "r", mfc = 'y')
plt.show()