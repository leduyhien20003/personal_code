'''
Câu 26. Một số được gọi là số mạnh mẽ khi nó đồng thời vừa chia hết
cho số nguyên tố và chia hết cho bình phương của số nguyên tố đó.
 Tìm số mạnh mẽ nhỏ hơn số N cho trước (N < 10000)
'''
def ktnt(n):
    if n<2: return 0 
    else: 
        for i in range (2,n):
            if n%i==0:
                return 0
        return 1

n = int(input('Nhập n = '))

for x in range(n ):
    for i in range(1, int(x/2) +1):
        if ktnt(i) and x % i == 0 \
                and x % (i * i) == 0:
            print(x, end=" ")
            break



