lst = []

repeat_time = int(input())
for i in range(repeat_time):
    tall, mass = map(int, input().split())
    lst.append((tall,mass))

rank = 0
for i in range(repeat_time):
    pop = lst.pop(i) #현재 비교해야할것을 리스트 항목에서 제외시킨다
    for element in lst: #남은 lst에서 iteration을 돌아준다
        if (pop[0] < element[0] and pop[1] < element[1]):
            rank+=1
    print(rank + 1, end =' ')
    rank = 0
    lst.insert(i, pop) #제외한 항목을 다시 추가해준다.