from sys import stdin
input = stdin.readline

count = 1 #무조건 한번은 회의 가능함.
lst = []
n = int(input().rstrip())
for _ in range(n):
    start, finish = map(int, input().rstrip().split())
    lst.append((start, finish))
srt = sorted(lst, key = lambda x : (x[1], x[0])) #끝나는 시간 오름차순으로 정렬, 끝나는 시간이 같다면 시작시간을 기준으로 정렬

#끝나는 시간이 그나마 빠른걸 선택한다. -> 그리드 알고리즘이지만 이것은 최적해가 보장된다고 할 수 있다.
pop = srt.pop(0)
tmp = pop
for element in srt:
    if(tmp[1] <= element[0]):
        count += 1
        tmp = element
print(count)