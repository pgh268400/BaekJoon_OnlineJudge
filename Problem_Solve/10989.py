from sys import stdin
counting = {}

n = int(stdin.readline())
for i in range(n):
    a = int(stdin.readline())
    if not a in counting:
        counting[a] = 1
    else:
        counting[a] += 1
for i in range(1, max(counting)+1):
    if i in counting:
        for j in range(counting[i]):
            print(i)