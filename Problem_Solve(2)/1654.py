#1654번 - 이분탐색 이용
#분기점은 랜선의 길이

lst = []
k,n = map(int, input().split())
for i in range(k):
    lan = int(input())
    lst.append(lan)
#print(lst)

def binary_search(data, target):

    start,end = 1, max(data)
    lst = []
    while start <= end:
        mid = (start + end) // 2
        result = 0
        for element in data:    
            result += element // mid
        if result >= target:
            lst.append(mid)
            start = mid + 1
        elif result < target: #목표보다 덜 만들어졌으면
            end = mid - 1 #더 작은수로 나눈다.
        else:
            start = mid + 1
    return lst

result = binary_search(lst, n)
print(max(result))