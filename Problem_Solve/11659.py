from sys import stdin
input = stdin.readline

n,m = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
prefix_sum = [0] #구간합 배열
for element in lst:
    last = prefix_sum[-1]
    prefix_sum.append(last + element)

for _ in range(m):
    r1, r2 = map(int, input().rstrip().split())
    r1 -= 1
    r2 -= 1
    print(prefix_sum[r2+1] - prefix_sum[r1])