#나무자르기 - 예전에 썼던거 날먹하기!


k,n = map(int, input().split())
lst = list(map(int, input().split()))


def binary_search(data, target):
    start,end = 0, max(data)
    lst = []
    while start <= end:
        mid = (start + end) // 2
        result = 0
        for element in data:
            if(element > mid):
                tmp = element - mid
                result += tmp
                
        if result >= target:
            lst.append(mid)
            start = mid + 1 #더 큰값을 찾기 위해 더 큰수로도 나눠본다.
        elif result < target: #목표보다 덜 만들어졌으면
            end = mid - 1 #더 작은수로 나눈다.
    return lst

result = binary_search(lst, n)
print(max(result))