from collections import deque #deck 사용을 위해 import

case = int(input())

for _ in range(case):
    result = []
    
    n,m = map(int, input().split())
    queue = deque(map(int, input().split()))
    position = [i for i in range(0, n)]


    while True:
        pop = queue.popleft() #제일처음에 들어온 값 제거
        if(len(queue) == 0):
            break
        if(pop < max(queue)): #뽑은것보다 중요도가 높은값이 존재하면
            queue.append(pop) #가장뒤에 배치
            position.append(position.pop(0))
        else:
            result.append(position.pop(0))
    result = result + position
    print(result.index(m) + 1)