from sys import stdin
time = int(stdin.readline().rstrip())
lst = []
for i in range(time):
    x,y = map(int, stdin.readline().rstrip().split())
    lst.append ((y,x))
lst.sort()
for y, x in lst:
    a = x
    b = y
    print(a, b)