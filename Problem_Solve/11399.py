from sys import stdin
input = stdin.readline

dic = {}
n = int(input().rstrip())
time = list(map(int, input().rstrip().split()))

time.sort()
#print(time)

total = 0

for j in range(1, n+1):
    for i in range(j):
        total += time[i]
print(total)