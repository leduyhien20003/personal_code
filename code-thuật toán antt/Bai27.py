'''
Câu 27. Viết chương trình in ra các cặp số (a,b) thoả mãn điều kiện 0<a,b<1000,
sao cho ước chung lớn nhất của 2 số đó là một số nguyên tố.
'''
def ktnt(n):
    if n<2: return 0 
    else: 
        for i in range (2,n):
            if n%i==0:
                return 0
        return 1


def gcd(a,b):
    while b>0:
        r=a%b
        a=b
        b=r
    return a

a =int(input('Nhập a = '))
b=int(input('Nhập b = '))
c = []
for i in range(a+1, b):
    for j in range(a+1, b):
        if ktnt(gcd(i, j)):
            c.append({(i, j): gcd(i, j)})
   
print(c)