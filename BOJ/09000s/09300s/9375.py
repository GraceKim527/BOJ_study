import sys
from collections import Counter
input = sys.stdin.readline

t = int(input()) # 테스트 케이스

for _ in range(t):
    n = int(input()) 
    clothes = []
    for j in range(n):
        a, b = input().split()
        clothes.append(b)

    cloth_counter = Counter(clothes)
    cnt = 1

    for key in cloth_counter:
        cnt *= cloth_counter[key] + 1
    
    print(cnt - 1)
