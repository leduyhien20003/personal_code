"""
Câu 10. Viết chương trình đếm số ước và
 số ước nguyên tố của một số N nhập vào từ bàn phím.
"""

n=int(input('Nhập N = '))

def ktnt(n):
	if n<2: return 0 
	else: 
		for i in range (2,n):
			if n%i==0:
				return 0
		return 1
s=0
q=0        
for i in range (1,n+1) :
	if n%i==0:
		s+=1
	if n%i==0 and ktnt(i):
		q+=1
print('Số ước: ',s)
print('Số ước nguyên tố : ',q)