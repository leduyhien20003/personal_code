"""
Câu 5. Viết chương trình tính tổng của các số nguyên tố nằm trong khoảng [A, B] với A, B nhập
vào từ bàn phím.
"""
import math
a=int(input('Nhập A = '))
b=int(input('Nhập B = '))
def ktnt(n):
    if n<2: return 0 
    else: 
        for i in range (2,n):
            if n%i==0:
                return 0
        return 1
t=0     
c=[]
for i in range (a,b+1):
    if ktnt(i):
        c.append(i) 
          
print(sum(c))