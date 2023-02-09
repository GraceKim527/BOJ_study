from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return


for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1
    
    print(cnt)