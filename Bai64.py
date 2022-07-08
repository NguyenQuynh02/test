import matplotlib.pyplot as plt
import numpy as np
with open("D:/DATA63.txt") as f:
    x = np.array(f.readline().split()).astype(float)
    y = np.array(f.readline().split()).astype(float)

plt.subplot(1,3,1)
plt.title("BAR CHART")
plt.grid(axis="y", color="g", linestyle = ":")
plt.xlabel("X axis", loc="right")
plt.ylabel("Y axis", loc="top")
plt.bar(x, y, color="r" )

plt.subplot(1,3,2)
plt.title("HISTOGRAM CHART")
plt.grid(axis="y", color = "g", linestyle = ":")
plt.xlabel("X axis", loc = "right")
plt.ylabel("Y axis", loc="top")
plt.hist( y, color="g")

plt.subplot(1,3,3)
plt.title("PIE CHART")
plt.pie(y, startangle=90)



plt.show()

