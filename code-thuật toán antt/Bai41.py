'''
Câu 41. Cho các số nguyên dương a,k,n, nhập từ bàn phím (0<a,k<n<1000), Viết chương trình
xác định xem a^k mod n có phải là một số nguyên tố hay không
(sử dụng thuật toán bình phương và nhân có lặp)?
'''
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def square_integer(number_a, number_k, number_n):
    k = []
    while number_k > 0:
        k.append(int(number_k % 2))
        number_k = int(number_k // 2)
    a = number_a
    if k[0] == 1:
        b = a
    else:
        b = 0
    for i in range(1, len(k)):
        a = (a * a) % number_n
        if k[i] == 1:
            b = (b * a) % number_n
    return b


number_a = int(input('Nhập số a > 0 = '))
number_k = int(input('Nhập k = '))
number_n = int(input(f'Nhập n > {number_k} = '))
b = square_integer(number_a, number_k, number_n)
if b % 2 == 0:
    print('NO')
else:
    if (is_prime(b)):
        print('YES')
    else:
        print('NO')