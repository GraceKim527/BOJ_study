from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
card = [input().rstrip() for _ in range(n)]
res = set()
for per in permutations(card, k):
    res.add(''.join(per))

print(len(res))