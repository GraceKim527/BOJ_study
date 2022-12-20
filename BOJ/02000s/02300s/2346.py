import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
d = deque(enumerate(map(int, input().split()), start=1))

for i in range(N):
    p = d.popleft()
    print(p[0], end=' ')
    if p[1] > 0:
        d.rotate(-(p[1] - 1))
    else:
        d.rotate(-p[1])