import numpy as np
c = np.array([2, 4, 6, 8, 2, 9, 12])
k = np.where(c % 2 == 0)
print("Các phần tử có chỉ số chẵn trong c: ", k)
print("Tổng các số chẵn trong c = ", k.sum())