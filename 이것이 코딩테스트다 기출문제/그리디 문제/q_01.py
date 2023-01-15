import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0 # 전체 그룹
count = 0 # 모험가 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함
    if count >= i: 
        result += 1
        count = 0

print(result)