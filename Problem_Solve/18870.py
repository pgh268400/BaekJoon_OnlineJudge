from sys import stdin
input = stdin.readline

result = {}
index = 0

n = int(input())
lst = list(map(int, input().rstrip().split()))
srt = sorted(lst)

for i in range(n):
    item = srt[i]
    if not item in result:
        result[item] = index
        index += 1
#print(result)
for element in lst:
    print(result[element], end = ' ')