import math
from sys import stdin
input = stdin.readline

while True:
    n = int(input())
    if(n == 0):
        break
    prime = set([i for i in range(n + 1, 2 * n + 1)])
    prime.discard(1) #1 안전하게 지우기

    for i in range(2, int(math.sqrt(2 * n)) + 1):
        j = 2
        while(i * j <= 2 * n):
            prime.discard(i * j)
            j += 1
    print(len(prime))