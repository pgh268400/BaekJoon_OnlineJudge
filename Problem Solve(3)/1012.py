from sys import stdin
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    #현재 좌표의 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        graph[x][y] = 0 #방문처리
        
        #상하좌우도 dfs 탐색을 진행한다.
        #각각 진행하면서 그것이 또 상하좌우를 호출할 것이며
        #방문하지 않은것을 모두 찾아서 채워준다.
        #즉 0의 묶음이 상하좌우 호출이후 모두 사라진다.
        dfs(x-1, y)
        dfs(x , y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

T = int(stdin.readline().rstrip())
for _ in range(T):
    M,N,K = map(int, stdin.readline().rstrip().split())
    graph = [[0] * M for i in range(N)]

    for i in range(K):
        x,y = map(int, stdin.readline().rstrip().split())
        graph[y][x] = 1
    #print(graph)

    result = 0
    for i in range(N):
        for j in range(M):
            if (dfs(i,j) == True):
                result += 1
    print(result)