#01타일 = 피보나치 수열과 동일 
#d[i] = d[i-1] + d[i - 2]
import sys

fib = [0, 1,2,3,5] + [0] * (10 ** 6 - 4)

def fibo(n):
    for i in range(5, n+1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % 15746
    return fib[n]

num = int(input())
print(fibo(num))