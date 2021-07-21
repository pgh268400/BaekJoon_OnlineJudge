#순열을 위해 Import
from itertools import combinations
result = []

n,m = map(int, input().split())
card = list(map(int, input().split()))
comb = list(combinations(card, 3)) #3장씩 뽑는 모든 조합 만들기

for a,b,c in comb:
    total = a+b+c
    if(total <= m): #범위내에 들어가면
        result.append(total) #append 한다.
print(max(result)) #max값 출력한다.