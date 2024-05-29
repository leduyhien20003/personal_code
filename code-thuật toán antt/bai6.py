"""
Câu 6. Hai số tạo thành một cặp số thân thiết khi chúng tuân theo quy luật: Số này bằng tổng tất
cả các ước của số kia (trừ chính số đó) và ngược lại. Viết chương trình tìm hai số dạng này nhỏ
hơn N (với N nhập vào từ bàn phím).

"""
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

n=int(input('Nhập n= '))


e=[]
for a in range(1,n):
    c=[]
    for i in range(1,a):
        if a%i==0:
            c.append(i)
        b=sum(c)
        d=[]
        
        for k in range(1,b):
            if b%k==0:
                d.append(k)
                if sum(d)==a and a<b:
                    e=[a,b]
print(e)



