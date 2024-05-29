'''
Câu 40. Cho mảng A nhập từ bàn phím gồm các số nguyên dương. Hãy viết chương trình đếm
các cặp số (i,j) trong mảng A sao cho ước chung lớn nhất của chúng là một số nguyên tố
'''
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


A = [int(x) for x in input().split()]
count = 0
for i in range(0, len(A)):
    for j in range(i, len(A)):
        if is_prime(gcd(A[i], A[j])):
            count += 1
print(count)