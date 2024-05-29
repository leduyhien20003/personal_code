"""
Câu 12. Viết chương trình tìm bốn số nguyên tố liên tiếp,
 sao cho tổng của chúng là số nguyên tố
nhỏ hơn hoặc bằng N (với N được nhập vào từ bàn phím).
"""


n=int(input('Nhập n = '))

def ktnt(n):
    if n<2: return 0 
    else: 
        for i in range (2,n):
            if n%i==0:
                return 0
        return 1
a=[]        
for i in range (1,n+1):
    if ktnt(i):
       a.append(i)
      
for i in  (0, len(a)+1):
    b=sum(a[i:i+4]) 
    if ktnt(b) :
        print(a[i:i+4], end= ' ')