from sys import stdin
time = int(stdin.readline().rstrip())
lst = []
for i in range(time):
    x,y = map(int, stdin.readline().rstrip().split())
    lst.append ((x,y))
lst.sort()
for x,y in lst:
    print(x, y)