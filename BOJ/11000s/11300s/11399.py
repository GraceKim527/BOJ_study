n = int(input()) # 사람 수
p = list(map(int, input().split())) # 돈 인출하는 데 걸리는 시간
num = 0
p.sort()
for i in range(n):
    for j in range(i + 1):
        num += p[j]
print(num)