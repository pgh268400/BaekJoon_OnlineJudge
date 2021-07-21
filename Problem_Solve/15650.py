from itertools import combinations

N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]

if M == 1:
    for i in range(N):
        print(lst[i])
else:
    comb = combinations(lst, M)
    for element in comb:
        convert = str(element)
        convert = convert.replace("(", "")
        convert = convert.replace(")", "")
        convert = convert.replace(", ", " ")
        print(convert)