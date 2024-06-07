import sys 
input = sys.stdin.readline

def round_cal(val):
  if val - int(val) >= 0.5:
    return int(val) + 1
  else:
    return int(val)

n = int(input())

if n:
  level = []
  for _ in range(n):
    level.append(int(input().rstrip()))
    
  nn = round_cal(n * 0.15)
  level.sort()
  if nn > 0:
    print(round_cal(sum(level[nn: -nn]) / len(level[nn: -nn])))
  else:
    print(round_cal(sum(level) / len(level)))
else:
  print(0)
