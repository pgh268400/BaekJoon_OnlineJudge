#Queue 를 통한 BFS 구현

from collections import deque

def bfs(graph, start, visited):
    #Queue에 넣고,
    queue = deque([start]) #(덱을 이용한 Queue 구현)
    #현재 노드를 방문처리
    visited[start] = True
    
    while queue:
        #큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft() #Queue의 가장 앞에있는것 뽑기.
        print(v, end = ' ')
        graph[v].sort() #그래프 순회전 정렬 (작은숫자 먼저 탐색해야함.)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i) #Child node 순회를 쭉돌면서 방문처리
                visited[i] = True

#재귀함수를 통한 dfs 구현

def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v, end = ' ')
    graph[v].sort() #그래프 순회전 정렬 (작은숫자 먼저 탐색해야함.)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#기준 - 인접노드중 작은값부터
n,m,v = map(int, input().split())

graph = [[] for row in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    #간선은 양방향이다.
    graph[a].append(b)
    graph[b].append(a)

# 각 노드가 방문된 정보를 표현
visited = [False] * (n+1) #초기값은 전부 방문하지 않음.
visited_2 = [False] * (n+1)

dfs(graph, v, visited)
print()
bfs(graph, v, visited_2)