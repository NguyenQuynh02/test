import matplotlib.pyplot as mp
import numpy as np
lable =["Nhãn", "Xoài", "Dứa", "Chuối", "Cam", "Bưởi"]
data = np.array([5800, 3200, 1200, 1700, 2400, 980])
explode = [0.3, 0.1, 0.5, 0, 0.6, 0.2]
color  =("orange", "cyan", "brown", "grey", "indigo", "beige")
wp = {"linewidth": 1, "edgecolor": "green"}
mp.title("Biểu đồ sả lượng")
mp.pie(data, labels=lable, explode=explode, colors=color, wedgeprops=wp, shadow=True, autopct="%.2f")
mp.show()