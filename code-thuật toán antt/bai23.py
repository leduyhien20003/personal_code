'''
Câu 23. Viết chương trình in ra màn hình YES trong trường hợp tổng
của các số nguyên tố trong khoảng [A, B] là cũng là một số nguyên tố
và NO nếu ngược lại. Với A,B là hai số được nhập vào từ bàn phím.
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


def sum(number_a, number_b):
    value = 0
    for i in range(number_a, number_b + 1):
        value += i
    return value


number_a = int(input('Nhập số a = '))
number_b = int(input('Nhập số b = '))
if is_prime(sum(number_a, number_b)):
    print('YES')
else:
    print('NO')