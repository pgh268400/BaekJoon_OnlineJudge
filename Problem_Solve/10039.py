a = int(input())
b = int(input())
c = int(input())
d = int(input())
f = int(input())

if(a < 40):
    a = 40
if(b < 40):
    b = 40
if(c < 40):
    c = 40
if(d < 40):
    d = 40
if(f < 40):
    f = 40
print(sum([a,b,c,d,f]) // 5)