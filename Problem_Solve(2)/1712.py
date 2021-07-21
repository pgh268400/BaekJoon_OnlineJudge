lst = []
lst = list(map(int, input().split()))
#고정비용, 원가, 판매가
hold = lst[0]
origin = lst[1]
sell = lst[2]

if (origin >= sell): #만약 물건을 원가랑 같게 팔거나 더 싸게팔면
    print("-1") #손익분기점은 존재하지 않는다.
else:
    profit = sell - origin #수익
    profit_count = hold / profit + 1
    print(int(profit_count))