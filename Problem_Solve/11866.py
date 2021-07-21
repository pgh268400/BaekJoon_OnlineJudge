n,k = map(int, input().split())
lst = [i for i in range(1, n+1)]
print("<", end= '')
for i in range(0, n):
    for j in range(0, k-1):
        lst.append(lst.pop(0))
    if(i == n - 1):
        print(lst.pop(0), end = '>')
    else:
        print(lst.pop(0), end = ', ')