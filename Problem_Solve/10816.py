from collections import Counter

n = int(input())
card1 = map(int , input().split())
m = int(input())
card2 = map(int , input().split())
c = Counter(card1)
for el in card2:
    print(c[el], end= ' ')