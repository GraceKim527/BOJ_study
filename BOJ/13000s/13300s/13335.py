import sys 
from collections import deque
input = sys.stdin.readline

# n은 트럭 수, w은 다리 올라갈 수 있는 트럭 수, l은 최대 하중
n, w, l = map(int, input().split()) 
weight = list(map(int, input().split()))

temp = [0] * w
time = 0 

while temp:
  time += 1
  temp.pop(0) # 첫번째 요소 pop
  if weight:
    if sum(temp) + weight[0] <= l:
      temp.append(weight.pop(0))
    else:
      temp.append(0)
      
print(time)