from sys import stdin
input = stdin.readline

from collections import deque
cavin = {}

def bfs(start):
    result = 0
    dic = {}
    visited = [False] * (N+1)

    queue = deque([start])
    visited[start] = True
    dic[start] = 0 #탐색거리 저장용

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                dic[i] = dic[v] + 1
                queue.append(i)
                visited[i] = True
    for key, value in dic.items():
        result += value
    return result

N,M = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    #a와 b가 친구관계 - 그래프 양방향 연결.
    a,b = map(int, input().rstrip().split())    
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    r = bfs(i)
    cavin[i] = r
#먼저 케빈베이컨 값 순으로 오름차순 정렬하고 같아지면 번호가 작은걸로 정렬함.
sorted_cavin = sorted(cavin.items(), key = lambda x : (x[1], x[0]))
print(sorted_cavin[0][0])