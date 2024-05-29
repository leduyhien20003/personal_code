'''
Câu 24. Đặt S1, S2 là các mảng chứa giá trị bình phương của các số nguyên.
Hãy viết chương trình in ra số lượng tất cả các số nguyên tố nằm trong
khoảng [a,b] sao cho số này cũng là tổng của hai số x và y với x thuộc
S1 và y thuộc S2. Trong đó, a,b là các số được nhập từ bàn phím
Ví dụ: với a=10, b =15, in ra giá trị là 1 vì trong khoảng [10,15]
chỉ có 2 số nguyên tố 11 và 13, nhưng chỉ có 13 = 2^2 + 3^2=4+9.

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


def count_number_prime(number_a, number_b, S1, S2):
    S = []
    for i in S1:
        for j in S2:
            sum = i + j
            if sum >= number_a and sum <= number_b \
                    and is_prime(sum) and sum not in S:
                S.append(sum)
    return S


number_a = int(input('Nhập số a = '))
number_b = int(input(f'Nhập số b >= '
                     f'{number_a} = '))

if number_b >= number_a:
    q = int(math.sqrt(number_b))
    S1 = [x * x for x in range(1, q + 1)]
    S2 = [x * x for x in range(1, q + 1)]
    result = count_number_prime(number_a, number_b, S1, S2)
    if len(result) > 0:
        print(result)
        print(f'Số lượng : {len(result)}')
    else:
        print('Không có giá trị nào')
else:
    print('Thử Lại')