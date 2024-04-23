import sys 
input = sys.stdin.readline

N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수
mapBoard = [[0] * (N+1) for _ in range(N+1)] # 맵 n+1 x n+1
direction_info = [] # 방향 회전

# 맵 정보
for _ in range(K):
  row, column = map(int, input().split())
  mapBoard[row][column] = 1 # 사과가 있는 곳의 값

# 방향 회전 정보
L = int(input()) # 뱀의 방향 변환
for _ in range(L):
  # X(게임 시작 시간으로부터 X초가 끝난 후)는 정수, C(L은 왼쪽, D은 오른쪽)는 문자
  X, C = input().split()
  direction_info.append((int(X), C))
  
# 동, 남, 서, 북확인
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
  if c == "L":
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4
  
  return direction

def simulation():
  x, y = 1, 1 # 뱀 머리 위치
  mapBoard[x][y] = 2 # 뱀이 존재하는 위치 
  direction = 0 # 동쪽
  time = 0 # 시간
  index = 0 # 회전 정보
  q = [(x, y)] # 뱀이 차지하고 있는 위치 정보
  
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 맵 범위 내, 뱀이 몸통이 없는 위치라면
    if 1 <= nx and nx <= N and 1 <= ny and ny <= N and mapBoard[nx][ny] != 2:
      # 사과가 없다면 꼬리 없애기
      if mapBoard[nx][ny] == 0:
        mapBoard[nx][ny] = 2
        q.append((nx, ny))
        px, py = q.pop(0)
        mapBoard[px][py] = 0
      # 사과가 있다면 
      if mapBoard[nx][ny] == 1:
        mapBoard[nx][ny] = 2
        q.append((nx, ny))
    # 벽에 부딪혔다면 끝.
    else:
      time += 1
      break
    
    x, y = nx, ny # 현재 위치를 넣어준다.
    time += 1 # 시간도 추가
    if time <= direction_info[-1][0]: # index 예외처리
      if time == direction_info[index][0]:
        direction = turn(direction, direction_info[index][1])
        index += 1
      
  return time

print(simulation())