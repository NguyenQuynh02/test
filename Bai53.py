import numpy as np
def vecinput(n , name):
    print("Nhập mảng : ")
    a = np.random.rand(n)
    for i in range(n):
        a[i] = float(input(name + "[{}] = ".format(i)))
    return a


n = int(input("n= "))
a = vecinput(n, "a")

try:
    t = int(input("Nhập số dòng của ma trận: "))
    if n % t !=0: raise ValueError
    k = a.reshape(t, n //t)
    print("Ma trận thu được : \n", k)
except:
    print(ValueError, "Không thể reshape ma trận!")

 # tach a , cot 1 = mang b , cot 2 = mang c

b = np.array([9,3,7])
c = np.array([2,3,4])

# nối 2 mảng b,c thành d
d = np.concatenate((b,c))
print("Mảng d: ", d)

# vị trí lớn hơn 1 trong d
k = np.where(d>1)
print("Vịt trí các phần tử lớn hơn 1 trong d: ", k[0])

# sắp tăng = heapsort
d = np.sort(d, kind="heapsort")
print("d đã đc sắp heapsort: ", d)

# chèn k vào vào d , cho biêt vị trí của k, ko phá vỡ tính sắp xếp

k = int(input("Nhập giá trị k cần chèn k  = "))
vt = np.searchsorted(d, k)
print("Vị trí muốn chèn: ", vt) # tự chọn vt thích hợp để chèn ko thay đổi tihs tăng dần
d = np.insert(d, vt, k)
print("Mảng sau khi chèn: ", d)