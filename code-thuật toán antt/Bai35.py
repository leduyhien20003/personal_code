'''
Câu 35. Cài đặt thuật toán kiểm tra số nguyên tố Miller-Rabin in ra kết luận
về 1 số nguyên dương N nhập vào từ bàn phím với xác suất kết luận tương
 ứng sau thuật toán.
'''


def square_integer(number_a, number_k, number_n):
    k = []
    while number_k > 0:
        r = number_k % 2
        k.append(r)
        number_k //= 2
    a = number_a
    if k[0] == 1:
        b = a
    else:
        b = 1
    for i in range(1, len(k)):
        a = (a * a) % number_n
        if k[i] == 1:
            b = (b * a) % number_n
    return b


def miller_rabin(n, t):
    r = n - 1
    s = 0
    while r % 2 == 0:
        s += 1
        r //= 2
    k = 1
    for i in range(2, n - 2):
        a = i
        y = square_integer(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = (y * y) % n
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
        if k >= t:
            break
        k += 1
    return True


n = int(input('Nhập n = '))
t = int(input('Nhập t = '))
if miller_rabin(n, t):
    print('NT')
else:
    print('HS')