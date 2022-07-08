import numpy as np
n = int(input(" n = "))
a = np.random.rand(n)
print("a = ", a)
print("Số chiều của a: ", a.ndim)
print("Kích thước của mỗi chiều: ", a.shape)
print("Độ dài của \6666a : ", len(a))
print("Kích thước của mục trong mảng đó: ", a.itemsize)
print("Kiểu của a : ", a.dtype)


# lấy 100 ptu từ đoạn 1-n
b = np.linspace(1, n , 100)
print("MẢNG b = ", b)
print("Số chiều của b: ", b.ndim)
print("Kích thước của mỗi chiều: ", b.shape)
print("Độ dài của b: ", len(b))
print("Kích thước của mục trong mảng đó: ", b.itemsize)
print("Kiểu của a : ", b.dtype)

# c với 100 số chẵn đầu tiên
c = np.arange(2, 202, 2)
print("Mảng c : ", c )

# d  với 100 phần tử 1
d = np.ones(100)
print("Mảng d :", d )

# e với 100 phần tử 0
e = np.zeros(100)
print("Mảng e : ", e)

# h với 100 phtu theo phan bố gauss
h = np.random.randn(100)
print("Mảng h :", h )

 # ma trận k gồm n m số 1
m = int(input("m = "))
k = np.ones((n,m) )
print("Ma trận K:\n ", k)

# p là ma trận đơn vị n m
e = np.eye(n,m)
print("Ma trận e:\n", e)

# q là ma trận đường chéo là mảng a
q = np.diag(a)
print("Ma trận q:\n ", q)