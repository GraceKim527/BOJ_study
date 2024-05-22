import sys 
input = sys.stdin.readline

h, w = map(int, input().split()) # h x w 개의 구역

sky = []
for i in range(h):
  sky.append(list(input().rstrip()))
  
result = [[0] * w for _ in range(h)]

for i in range(h):
  cnt = 1
  cloud = False
  for j in range(w):
    if not cloud and sky[i][j] == '.':
      result[i][j] = -1
    elif sky[i][j] == 'c':
      cloud = True
      result[i][j] = 0
      cnt = 1
    elif cloud and sky[i][j] == '.':
      result[i][j] = cnt
      cnt += 1
      
for i in result:
  print(*i, end= ' ')
  print()