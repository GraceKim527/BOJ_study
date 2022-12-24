import sys
input = sys.stdin.readline

N, length = map(int,input().split()) # 과일의 개수, 스네이크버드의 초기 길이
height = list(map(int, input().split())) # 과일 높이

height.sort()
for h in height: 
    if length >= h:
        length += 1
    else:
        continue

print(length)