"""
Câu 2. Viết chương trình tìm các số nguyên tố có N chữ số với N nhập từ bàn phím và 2 ≤ N ≤
10
"""
import math
n=int(input('Nhập n = '))
a=10**(n-1)
b=10**n 

def ktnt(n):
    if n<2: return 0 
    else: 
        for i in range (2,n):
            if n%i==0:
                return 0
        return 1
c=[]        

for i in range (a,b+1):
    if ktnt(i):
        c.append(i)    
print(c)    