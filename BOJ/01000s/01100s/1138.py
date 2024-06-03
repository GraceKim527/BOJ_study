import sys 
input = sys.stdin.readline

N = int(input())
users = list(map(int, input().split()))
answer = [0] * N

for i in range(N):
  cnt = 0
  for j in range(N):
    if cnt == users[i] and answer[j] == 0:
      answer[j] = i + 1
      break
    elif answer[j] == 0:
      cnt += 1
      
print(' '.join(map(str, answer)))