#재귀함수를 통한 dfs 구현
import sys
sys.setrecursionlimit(10**6) #재귀 깊이 설정

from sys import stdin
input = stdin.readline

get_virus = 0
def dfs(graph, v, visited):
    global get_virus
    
    visited[v] = True
    #print(v, end = ' ')
    if(v != 1):
        get_virus+=1
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n = int(input().rstrip())
r = int(input().rstrip())

graph = [[] for row in range(n+1)]

for _ in range(r):
    a,b = map(int, input().rstrip().split())
    #간선은 양방향이다.
    graph[a].append(b)
    graph[b].append(a)

# 각 노드가 방문된 정보를 표현
visited = [False] * (n+1) #초기값은 전부 방문하지 않음.

dfs(graph, 1, visited) #1번 컴퓨터가 웜 바이러스에 걸림.
print(get_virus)