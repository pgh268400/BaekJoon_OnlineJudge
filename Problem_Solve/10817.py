a,b,c = map(int,input().split())
l = [a,b,c]
l.remove(max(l))
print(max(l))