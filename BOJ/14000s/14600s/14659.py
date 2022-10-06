import sys
input = sys.stdin.readline

n = int(input()) # 활잡이의 수
hills = list(map(int, input().split())) # 봉우리에 있는 활잡이들

cnt = 0
maxHills = 0
ans = 0
for hill in hills:
    if hill > maxHills:
        maxHills = hill
        cnt = 0
    else:
        cnt +=1
    ans = max(ans, cnt)

print(ans)