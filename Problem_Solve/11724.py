#재귀함수를 통한 dfs 구현
from sys import stdin
import sys
sys.setrecursionlimit(10**6) #재귀 깊이 설정

def dfs(graph, v, visited):
    #현재 노드를 방문처리
    if (visited[v] == True): #이미 방문했으면 탐색하지 않음.
        return False
    visited[v] = True
    #print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            #print(visited)
    #탐색 전부 종료시
    return True
#기준 - 인접노드중 작은값부터
n,m = map(int, stdin.readline().rstrip().split())

graph = [[] for row in range(n+1)]

for _ in range(m):
    a,b = map(int, stdin.readline().rstrip().split())
    #간선은 양방향이다.
    graph[a].append(b)
    graph[b].append(a)
#print(graph)
# 각 노드가 방문된 정보를 표현
visited = [False] * (n+1) #초기값은 전부 방문하지 않음.

cc = 0
for i in range(1, n+1):
    if dfs(graph, i, visited) == True:
        cc += 1
print(cc)