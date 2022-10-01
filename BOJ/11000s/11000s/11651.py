import sys
input = sys.stdin.readline

n = int(input()) # N개의 점
li = []

for i in range(n):
    x, y = map(int, input().split())
    li.append([y, x])

li = sorted(li)

for y, x in li:
    print(x, y)