from itertools import permutations

N, M = map(int, input().split())
lst = list(map(int, input().split()))

#사전순을 위해 미리 정렬함.
lst.sort()

if M == 1:
    for i in range(N):
        print(lst[i])
else:
    comb = permutations(lst, M)
    for element in comb:
        convert = str(element)
        convert = convert.replace("(", "")
        convert = convert.replace(")", "")
        convert = convert.replace(", ", " ")
        print(convert)