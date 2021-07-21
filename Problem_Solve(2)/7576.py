#Queue 를 통한 BFS 구현
from collections import deque
from sys import stdin
input = stdin.readline
mx = 0
def bfs(carrot):
    queue = deque() #(덱을 이용한 Queue 구현)
    for x,y in carrot:
        queue.append((x,y))
    while queue: #queue가 빌때까지 반복
        x,y = queue.popleft() #Queue의 가장 앞에있는것 뽑기.
        
        #4방향으로 당근을 익게 만든다.
        for i in range(4): #4방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            
            #좌표를 벗어났으면 무시
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            
            #토마토의 빈 부분, 익은 부분은 무시
            if farm[ny][nx] == -1 or farm[ny][nx] != 0:
                continue
            #안익었다면
            if farm[ny][nx] == 0:
                farm[ny][nx] = farm[y][x] + 1 #이전값의 + 1 해준다.
                queue.append((nx,ny))

all_ripe = True

farm = []
m,n = map(int, input().rstrip().split())
for _ in range(n):
    data = list(map(int, input().rstrip().split()))
    farm.append(data)

#왼쪽, 오른쪽, 아래, 위
dx = [-1, 1, 0, 0]
dy = [0, 0 , -1 , 1]

carrot_position = []
for j in range(n):
    for i in range(m):
        if farm[j][i] == 1: 
            carrot_position.append((i, j)) #x,y 형식으로 추가.

bfs(carrot_position)
#print(farm)
for j in range(n):
    for i in range(m):
        if farm[j][i] == 0: #탐색이 끝났는데 0이 하나라도 나오면
            all_ripe = False #모두 익지 못했다.
            break
    if all_ripe == False:
        break

if (all_ripe == False):
    print(-1)
else:
    #print(max(max(farm)) - 1) <-- 리스트에서 각각 최대가 아니라 그냥 전체에서 최대를 구하는거임 ;
    for j in range(n):
        for i in range(m):
            if mx < farm[j][i]:
                mx = farm[j][i]
    print(mx - 1)