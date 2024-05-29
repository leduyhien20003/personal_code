"""
Câu 16. Viết chương trình tìm các số nguyên tố từ một
mảng sinh ngẫu nhiên có kích thước N,với N nhập vào
 từ bàn phím
"""
import math
import random


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(2, int(math.sqrt(number) + 1)):
            if number % i == 0: return False
    return True


def list_random_number(number_n, list_random):
    for i in range(number_n):
        list_random.append(int(random.random() * 100))


def show_result(list_random):
    list_prime = []
    for i in list_random:
        if is_prime(i):
            list_prime.append(i)
    return list_prime


number_n = int(input("Nhập n = "))
list_random = []
list_random_number(number_n, list_random)
print(list_random)

print(show_result(list_random))