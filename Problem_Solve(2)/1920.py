N = int(input())
N1 = set(list(map(int , input().split())))
M = int(input())
M1 = list(map(int , input().split()))
for num in M1:
    if num in N1:
        print(1)
    else:
        print(0)