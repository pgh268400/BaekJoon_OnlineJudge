from sys import stdin
input = stdin.readline

dic = {1:1,2:2}

n = int(input())
def fibo(n):
    if n in dic:
        return dic[n]
    else:
        dic[n] = fibo(n-1) + fibo(n-2)
        return dic[n]
#mod 10007
print(fibo(n) % 10007)