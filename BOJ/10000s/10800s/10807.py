import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))

v = int(input()) # 찾으려고 하는 정수

count = 0

for i in li:
    if i == v:
        count += 1
print(count)