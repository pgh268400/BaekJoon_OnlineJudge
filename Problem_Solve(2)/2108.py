# 시간개선 코드(Counter, stdin.readline 이용)
from sys import stdin
from collections import Counter

lst = []
n = int(stdin.readline())
for i in range(1, n+1):
    data = int(stdin.readline())
    lst.append(data)

# lst = []
# n = int(input())
# for i in range(1, n+1):
#     data = int(input())
#     lst.append(data)

#round 함수는 2번째 인자값이 없으면 소수점 첫쨰자리에서 반올림한다.
print(round(sum(lst) / n)) #산술평균

lst.sort() #중앙값을 구하기 위해 정렬
print(lst[n // 2]) #중앙값

#미리구현된 Python의 Counter 함수를 이용해 시간을 줄인다.
filtered = Counter(lst).most_common()
#print(filtered)

if(len(filtered) > 1): #최빈값이 여러개면
    if(filtered[0][1] == filtered[1][1]): #최빈값이 같은게 보이면
        print(filtered[1][0]) #두번째로 작은값 출력
    else: #같은게 보이지 않으면 걍 출력
        print(filtered[0][0])
else:
    print(filtered[0][0])

#범위
range_num = max(lst) - min(lst)
print(range_num)