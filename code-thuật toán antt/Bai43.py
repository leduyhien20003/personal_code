'''
Câu 43. Cho N nhập vào từ bàn phím (0<N<1000), sinh một số nguyên tố p<100. Hãy viết
chương trình tìm tất cả các số nguyên a<N sao cho a^p mod N là số nguyên tố
'''
import math
import random


def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            return False
    return True


def random_number():
    while True:
        num = random.randint(2, 100)
        if is_prime(num):
            return num


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


p = random_number()
n = int(input('Nhập n = '))
print(p)
for a in range(2, n):
    b = square_integer(a, p, n)
    if is_prime(b):
        print(f'{a}:{b} ', end=" ")