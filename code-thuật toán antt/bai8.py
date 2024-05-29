"""
Câu 8. Một số gọi là số Т-prime nếu có có đúng 3 ước nguyên dương.
Viết chương trình tìm các số Т-prime nhỏ hơn hoặc bằng N với N
cho trước nhập từ bàn phím.
"""


def isTprime(n):
  count = 0
  for i in range(1, n + 1):
    if n % i == 0:
      count += 1
  if count == 3:
    return True
  return False

n = int(input('Nhập n = '))
c=[]
for i in range(n + 1):
  if isTprime(i):
    c.append(i)
print(c)    
    