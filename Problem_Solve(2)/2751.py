from sys import stdin
repeat_time = int(stdin.readline().rstrip())
lst = []
for i in range(repeat_time):
    a = int(stdin.readline().rstrip())
    lst.append(a)
lst.sort()
for n in lst:
    print(n)