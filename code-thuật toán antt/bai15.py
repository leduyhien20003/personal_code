"""
Câu 15. Viết chương trình Hai số nguyên tố sinh đôi là hai số nguyên
tố hơn kém nhau 2 đơn vị.Tìm hai số nguyên tố sinh đôi nhỏ hơn hoặc
bằng N, với N được nhập vào từ bàn phím.
"""

def ktnt(n):
    if n<2: return 0 
    else: 
        for i in range (2,n):
            if n%i==0:
                return 0
        return 1

n = int(input("Nhập số n = "))

a = []
for i in range(2,n+1):
        if ktnt(i) and ktnt(i + 2):
            a.append((i, i + 2))
print(a)




