"""
Câu 14. Viết chương trình tìm số nguyên tố có ba chữ số,
biết rằng nếu viết số đó theo thứ tự ngược lại thì ta được
một số là lập phương của một số tự nhiên.
"""
def ktnt(n):
    if n<2: return 0 
    else: 
        for i in range (2,n):
            if n%i==0:
                return 0
        return 1
def ktcp(n):
    for i in range(1,n):
        if i**3==n:
            return 1
    return 0


n=1000
for i in range(100,n):
        if ktnt(i) == True:
            k = int(str(i)[::-1])
            if ktcp(k) == True:
                print(i, end =" ")