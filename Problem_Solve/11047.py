#그리드 알고리즘 - 각 순간별 최선의 선택을 한다.

result = 0

lst = []
coin, target = map(int, input().split())
for _ in range(coin):
    lst.append(int(input()))
#문제의 조건은 오름차순 고정이므로 내림차순으로 바꾼다.
lst.sort(reverse = True)

#동전 갯수를 최소로 만들기 위해 가장 큰 동전 값을 최적으로 택한다.
for element in lst:
    if element > target:
        continue
    else:
        result += target // element
        target = target % element
print(result)