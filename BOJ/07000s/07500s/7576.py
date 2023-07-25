from collections import deque
import sys 
input = sys.stdin.readline

M, N = map(int, input().split()) # M은 가로, N은 세로
graph = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])
# 상 하 좌 우
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

result = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])
            

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
                
bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
            
    result = max(result, max(i))

print(result - 1)