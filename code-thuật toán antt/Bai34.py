'''
Câu 34. Cài đặt thuật toán kiểm tra số nguyên tố Fermat.
Trong trường hợp số nào thì thuật toán cho kết quả kiểm tra sai
'''


def binary(number_k):
    k = []
    while number_k > 0:
        r = int(number_k % 2)
        k.append(r)
        number_k = number_k // 2
    k.reverse()
    return k


def squart_integer(number_a, number_k, number_n):
    k = binary(number_k)
    k.reverse()  # xét trọng số nho
    a = number_a
    if k[0] == 1:
        b = number_a
    else:
        b = 1
    for i in range(1, len(k)):
        a = (a * a) % number_n
        if k[i] == 1:
            b = (b * a) % number_n
    return b


def fermat(t, n):
    j = 1
    for i in range(2, n - 1):
        a = i
        r = squart_integer(a, n - 1, n)
        if r != 1:
            return False
        if j >= t:
            break
        j += 1
    return True


n = int(input('Nhập n = '))
t = int(input('Nhập t = '))
if fermat(t, n):
    print('SNT')
else:
    print('HS')