# DFS

import sys
input = sys.stdin.readline

n = int(input()) # 전체
a, b = map(int, input().split()) # 촌수계산해야하는 번호 둘
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = []

# 연결되어있는 노드들을 graph에 저장
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, num):
    num += 1
    visited[v] = True
    
    if v == b:
        result.append(num)
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)

dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)
