import sys 
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

def dfs(x):
    visited[x] = True
    
    for n in graph[x]:
        if not visited[n]:
            dfs(n)

for _ in range(M):
    # 쌍방향으로
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)



for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)