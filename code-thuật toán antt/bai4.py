"""
Câu 4. Viết chương trình đếm số số nguyên tố nằm trong khoảng [A,B]
với A, B nhập vào từ bàn phím
"""
import math

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i**2, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def main():
    a = int(input("Nhập A: "))
    b = int(input("Nhập B: "))
    
    primes = sieve_of_eratosthenes(b)
    primes = [p for p in primes if a <= p <= b]
    
    print(primes)
    
    print(f"Số số nguyên tố trong khoảng [{a},{b}] là: {len(primes)}")
    

if __name__ == "__main__":
    main()

