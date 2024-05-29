'''
Câu 21. Một số gọi là siêu số nguyên tố nếu số lượng các số nguyên tố
từ 1 đến X (ngoại trừ X) là một số nguyên tố. Hãy viết chương trình
đếm số lượng các siêu số nguyên tố này trong khoảng [A,B] cho trước
nhập từ bàn phím
'''
import math


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(2, int(math.sqrt(number) + 1)):
            if number % i == 0:
                return False
    return True


def super_prime(number_a, number_b):
    result_list = []
    for x in range(number_a, number_b + 1):
        count = 0
        for i in range(1, x):
            if is_prime(i):
                count += 1
        if is_prime(count):
            result_list.append(x)
    return result_list


number_a = int(input('Nhập số a = '))
number_b = int(input(f'Nhập số b  > {number_a} =  '))
if number_b >= number_a:
    result = super_prime(number_a, number_b)
    print(result)
    print(f'Có {len(result)} số siêu nguyên tố')
else:
    print('Thử Lại')