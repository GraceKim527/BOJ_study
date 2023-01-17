import sys
input = sys.stdin.readline

n = int(input()) # 동전 개수 
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)