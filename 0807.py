import numpy as np

def vecinput(n, name):
    print("Nhập mảng : ", name)
    a = np.random.rand(n)
    for i in range(n):
        a[i] = float(input(name + "[{}] = ". format(i)))
    return a

n = int(input("n = "))
a = vecinput(n, "a")
b = vecinput(n, "b")
c = a + b
print("Mảng c  tổng: ", c)
print("Mảng d hiệu:", a-b)
print("Mảng e tích : ", a*b)
print("Mảng f thương: ", a/b)

print("Tổng c: ", sum(c))
print("MAX trong c: ", max(c))
print("Min trong c: ", min(c))

# lấy ra các phtu chỉ số chẵn trong c, tính tổng chúng
k = c[0::2]
print("Các phần tử có chỉ số chẵn trong c: ", k)
print("Tổng các số chẵn trong c = ", k.sum())


# chuyển c thahf mảng 2 chiều
#s = c.reshape(2,2)
#print("Chuyển C thành mảng 2 chiều: \n", s)

try:
    t = int(input("Nhập số dòng của ma trận:" ))
    if n % t != 0: raise ValueError
    k =  c.reshape(t, n //t)
    print("Ma trận thu được : \n", k)
except:
    print(ValueError, ":Không thể reshape")

