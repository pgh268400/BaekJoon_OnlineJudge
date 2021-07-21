a = list(map(int,input().split()))
lst = []
for n in a:
    lst.append(int(str(n)[::-1]))
print(max(lst))