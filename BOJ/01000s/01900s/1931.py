import sys 
input = sys.stdin.readline

N = int(input()) # 회의 수
s = []
count = 0
for _ in range(N):
    start, end = map(int, input().split()) # 시작시간이 n, 끝시간이 m
    s.append([start, end])

s = sorted(s, key=lambda a: a[0])
s = sorted(s, key=lambda a: a[1])

end = 0
for i, j in s:
    if i >= end:
        count += 1
        end = j

print(count)