import sys 
input = sys.stdin.readline

N, M, B = map(int, input().split()) # NxM, B개의 블럭
block = []
for _ in range(N):
    block.append([int(x) for x in input().rstrip().split()])

ans = int(1e9)
gravel = 0

for i in range(257):
    use = 0 # 사용블럭
    take = 0 # 가져온 블럭
    for x in range(N):
        for y in range(M):
            if block[x][y] > i:
                take += block[x][y] - i
            else:
                use += i - block[x][y]
    
    if use > take + B:
        continue

    time = take * 2 + use

    if time <= ans:
        ans = time
        gravel = i

print(ans, gravel)
