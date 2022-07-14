import sys
input = sys.stdin.readline

n, m = map(int, input().split())    #n, m으로 나누어받고
colors = [] 

for _ in range(m):
    colors.append(int(input()))     # 색마다 갯수

start = 1
end = max(colors)
# 한 명이 가져가는 보석수를 탐색 -> 
while start <= end:
    mid = (start + end) // 2 # 한 사람이 가져가는 보석 수
    total = 0
    for color in colors:
        if color % mid == 0:
            total += color//mid  # 나누어지게되면
        else:
            total += (color//mid) + 1 #나누어지지 않으면
    
    if total > n:
        start = mid + 1
    else:
        end = mid - 1

print(start)