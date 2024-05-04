from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
road = [list(input().rstrip()) for _ in range(n)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
  for j in range(m):
    if road[i][j] == 'I':
      x, y = i, j
      road[i][j] == 'X'

q = deque([])
q.append((x, y))
ans = 0

while q:
  x, y = q.popleft()
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and road[nx][ny] != 'X':
      if road[nx][ny] == 'P':
        ans += 1
      road[nx][ny] = 'X'
      q.append((nx, ny))
      
if ans == 0:
  print('TT')
else:
  print(ans)