import sys 
input = sys.stdin.readline

x, y = map(int, input().split()) 
z = (100*y) // x # 소수점을 제외하여 승률을 구하는 법
left = 0
right = x
result = 0

if z >= 99: # 승률이 이미 99퍼이상이라면,
  print(-1)
  
else: 
  while left <= right:
    mid = (left + right) // 2
    if (100* (y + mid)) // (x + mid) > z:
      result = mid
      right = mid - 1
    else:
      left = mid + 1
  
  print(result)