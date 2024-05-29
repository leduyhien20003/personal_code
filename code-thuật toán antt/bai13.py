"""
Câu 13. Viết chương trình tìm hai số nguyên tố nhỏ hơn hoặc bằng N
với N nhập vào từ bàn phím, sao cho tổng và hiệu của chúng đều
là số nguyên tố.
"""
n=int(input('Nhập n = '))

def SNT( n ):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False 
    return True

for a in range(1,n+1):
  if SNT(a):
    for b in range(1,n+1):
      if SNT(b) and a>b :
        c=a+b
        d=a-b
        if SNT(c) and SNT(d):
          print(b)
          print(a)
