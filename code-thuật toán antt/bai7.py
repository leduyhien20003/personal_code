"""
Câu 7. Một số emirp là một số nguyên tố mà khi đảo ngược vị trí các chữ số của nó, ta cũng được
một số nguyên tố. Viết chương trình liệt kê các số emirp nhỏ hơn N với N nhập vào từ bàn phím.
"""

def ktnt(n):
    if n<2: return 0 
    else: 
        for i in range (2,n):
            if n%i==0:
                return 0
        return 1

n = int(input('Nhập n = '))
for i in range(10,n):
        if ktnt(i) == True:
            k = int(str(i)[::-1])
            if ktnt(k) == True:
                print(i, end =" ")

