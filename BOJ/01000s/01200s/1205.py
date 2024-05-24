import sys
input = sys.stdin.readline

# n은 기존 리스트에 올라간 점수, p는 랭킹 리스트에 올라갈 수 있는 점수 개수
n, teSu, p = map(int, input().split()) 

# 예외처리 1: 랭킹 리스트가 비어있다면 무조건 1등
if n:
  score = list(map(int, input().split()))
else:
  print(1)
  exit(0)

# 예외처리 2: n과 p가 같으면서 꼴찌보다 작거나 같으면 -1
if n == p and score[-1] >= teSu:
  print(-1)

else: 
  res = n + 1
  for i in range(n):
    if score[i] <= teSu:
      res = i + 1
      break
    
  print(res)