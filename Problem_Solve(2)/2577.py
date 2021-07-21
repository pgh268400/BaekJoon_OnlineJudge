l = []
a = int(input())
b = int(input())
c = int(input())

d = a*b*c
d = str(d)

for i in range(len(d)):
    l.append(int(d[i]))

for i in range(0,10):
    print(l.count(i))