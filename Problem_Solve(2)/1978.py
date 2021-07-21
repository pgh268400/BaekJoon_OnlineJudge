#1978번 - 또라토스테네스
import math

n = int(input())
N1 = set(list(map(int , input().split())))

if 1 in N1:
    N1.remove(1) #1을 제거한다

mx = max(N1)
for i in range(2, int(math.sqrt(mx) + 1)):
        #배수를 반복문 돌려서 전부 지워준다.
        j = 2
        while (i * j <= mx):
            if i * j in N1:
                N1.remove(i * j)
            j += 1 

print(len(N1))