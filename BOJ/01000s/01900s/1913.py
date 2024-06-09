import sys 
input = sys.stdin.readline

n = int(input())
find = int(input())
snail = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0] # 상, 우, 하, 좌 순서
dy = [0, 1, 0, -1]

num = 2
x = n // 2
y = n // 2
snail[x][y] = 1
repeat = 1

i = 0 # dx, dy 가리키는 변수

answer = [x+1, y+1]
while x!=0 or y!=0:
  flag = 0
  for _ in range(2):
    for _ in range(repeat):
      x += dx[i]
      y += dy[i]
      snail[x][y] = num
      
      if find == num:
        answer = [x+1, y+1]
        
      if x == 0 and y == 0:
        flag = 1
        break
      num += 1
      
    if flag == 1: break
    i = (i + 1) % 4
  repeat += 1
  
for i in snail:
  print(*i)
  
print(*answer)