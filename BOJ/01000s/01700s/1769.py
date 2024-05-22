import sys 
input = sys.stdin.readline

x = input().rstrip() # 큰 자연수
cnt = 0

while len(x) > 1:
  cnt += 1
  answer = 0
  for i in x:
    answer += int(i)
  
  x = str(answer)
  
print(cnt)

if int(x) % 3 == 0:
  print("YES")
else:
  print("NO")
