import sys
input = sys.stdin.readline

N, M = map(int, input().split())
x, y = [], []

for r in range(N):
    r = list(map(int ,input().split()))
    x.append(r)

for r in range(N):
    r = list(map(int , input().split()))
    y.append(r)

for r in range(N):
    for c in range(M):
        print(x[r][c] + y[r][c], end=' ')
    print()