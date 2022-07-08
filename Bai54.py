import numpy as np
# đọc file

def readFile(name):
    with open(name, mode="r", encoding="utf-8") as f:
        n , m = f.readline().split()
        n = int(n)
        m = int(m)
        a = []
        for i in range(n):
            k = f.readline().split()
            a.append(k)
        a = np.array(a)
        return a, n, m

a, n, m = readFile('D:/DATA54.txt')
print("Mảng: ", a)
print("Dòng: ", n)
print("Cột: ",m)


