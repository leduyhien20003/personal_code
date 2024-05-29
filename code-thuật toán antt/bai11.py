"""
Câu 11. Viết chương trình tính tổng của các số nguyên tố nhỏ hơn hoặc bằng N với N được nhập
từ bàn phím.
"""
N=int(input('Nhập n = '))
def ktnt(n):
	if n<2: return 0 
	else: 
		for i in range (2,n):
			if n%i==0:
				return 0
		return 1
t=0		
c=[]
for i in range (1,N+1):
	if ktnt(i):
		c.append(i)	
print(sum(c))
