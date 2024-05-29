"""
Câu 18. Áp dụng thuật toán đã được học để viết chương trình
tính tổng của hai số nguyên lớn,hiển thị dưới mạng mảng
và dạng số nguyên.
"""
#KO HIỂU KỸ :( XXXXXXXXXXXXXXXXXXXXXXX
import math


def array(number, t, W):
    list = []
    while t > 0:
        p = int(number // math.pow(2, W * (t - 1)))
        list.append(p)
        number = int(number % math.pow(2, W * (t - 1)))
        t -= 1
    return list


def value_array(array, t, W):
    sum = 0
    i = 0
    while t > 0:
        p = int(math.pow(2, W * (t - 1)) * array[i])
        sum += p
        t -= 1
        i += 1
    return sum


def sum_interge(array_a, array_b, t, W):
    array_c = []
    remeber = 0
    exp = int(math.pow(2, W))
    while t > 0:
        p = array_a[t - 1] + array_b[t - 1] + remeber
        array_c.append(int(p % exp))
        if p > exp:
            remeber = 1
        else:
            remeber = 0
        t -= 1
    array_c.reverse()
    return remeber, array_c


p = 2147483647
W = 8
m = math.ceil(math.log2(p))
t = math.ceil(m / W)
number_a = int(input('Nhập số a = '))
number_b = int(input('Nhập số b = '))
array_a = array(number_a, t, W)
array_b = array(number_b, t, W)
result = sum_interge(array_a, array_b, t, W)
print(result)
print(value_array(result[1],t,W))