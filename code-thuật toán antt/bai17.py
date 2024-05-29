"""
Câu 17. Viết chương trình tìm số nguyên dương x nhỏ nhất và nhỏ hơn N
 nhập từ bàn phím sao cho giá trị của biểu thức 𝐴𝑥2 + 𝐵𝑥 + 𝐶 là một số
 nguyên tố với A,B,C là các số nguyên nhập vào
từ bàn phím.
"""
import math


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(2,
                       int(math.sqrt(number) + 1)):
            if number % i == 0:
                return False
    return True


def expression(number_n, number_a,
               number_b, number_c):
    for x in range(1, number_n + 1):
        sum = number_a * x * x + number_b * x + number_c
        if is_prime(sum):
            return sum, x
    return None


number_n = int(input('Nhập n = '))
number_a = int(input('Nhập a = '))
number_b = int(input('Nhập b = '))
number_c = int(input('Nhập c = '))
result = expression(number_n, number_a,
                    number_b, number_c)
if result != None:
    print(f'SNT = {result[0]}')
    print(f'X = {result[1]}')
else:
    print('Không tồn tại số X')