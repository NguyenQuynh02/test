import numpy as np
import matplotlib.pyplot as plt
with open("D:/DATA63.txt") as f:
    x = np.array(f.readline().split()).astype(float)
    y = np.array(f.readline().split()).astype(float)
plt.title("SCATTER CHART")
plt.xlabel("Trục X", loc="right")
plt.ylabel("Trục Y", loc="top")
plt.grid(axis="y", color = "g", linestyle = ":", linewidth = 1.5)
plt.scatter(x, y, color = "orange", s = y*2)
plt.show()