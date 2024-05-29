"""
Câu 9. Viết chương trình đếm số số nguyên tố nhỏ hơn hoặc bằng N với N được nhập vào từ bàn
phím
"""

n=int(input('Nhập n = '))
def ktnt(n):
	if n<2: return 0 
	else: 
		for i in range (2,n):
			if n%i==0:
				return 0
		return 1
t=0		

for i in range (1,n+1):
	if ktnt(i):
		t+=1	
print(t)
