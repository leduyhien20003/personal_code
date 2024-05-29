"""
Câu 1 Một số gọi là Q-prime khi nó có đúng 4 ước số nguyên dương. Hãy viết chương trình in ra
các số Q-Prime nhỏ hơn hoặc bằng một số N cho trước nhập từ bàn phím.
"""


def isqprime(n):
  count = 0
  for i in range(1, n + 1):
    if n % i == 0:
      count += 1
  if count == 4:
    return True
  return False

n = int(input('Nhập n = '))
c=[]
for i in range(n + 1):
  if isqprime(i):
    c.append(i)
    
print(c)




