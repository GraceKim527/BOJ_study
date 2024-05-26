import sys 
input = sys.stdin.readline

n = int(input()) # 수열의 길이
prg = list(map(int, input().split()))

maximum = 0
plus = [1] * n
minus = [1] * n

# 증가 수열
for i in range(n - 1):
  if prg[i + 1] >= prg[i]:
    plus[i + 1] += plus[i]
  
# 감소 수열 
for i in range(n - 1):
  if prg[i + 1] <= prg[i]:
    minus[i + 1] += minus[i]
    
plus_max = max(plus)
minus_max = max(minus)
print(max(plus_max, minus_max))