lst = []
n = int(input())
for _ in range(n):
    lst.append(int(input()))
lst.sort()

for element in lst:
    print(element)