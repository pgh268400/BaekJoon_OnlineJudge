import math

M = int(input())
N = int(input())
lst = set([i for i in range(M, N+1)])

if 1 in lst:
    lst.remove(1)

for i in range(2, int(math.sqrt(N)) + 1):
        j = 2
        while (i * j <= N):
            if i * j in lst:
                lst.remove(i * j)
            j += 1
if not lst:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))