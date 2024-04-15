import sys 
input = sys.stdin.readline

# 물이 새는 곳 개수 N, 테이프의 길이 L
N, L = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

start = data[0]
# 필요한 테이프 개수
count = 1

for l in data[1:]:
    # 범위 내에 물이 새는 곳이 있는지 여부 판단
    if l in range(start, start+L):
        continue
    else:
        start = l
        count += 1
        
        
print(count)