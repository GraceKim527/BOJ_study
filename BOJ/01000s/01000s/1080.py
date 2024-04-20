import sys 
input = sys.stdin.readline

a = []
b = []

n, m = map(int, input().split()) # 행렬의 크기 n, m
for _ in range(n):
    a.append(list(map(int, input().strip())))

for _ in range(n):
    b.append(list(map(int, input().strip())))


def check(i, j): # 뒤집기 휫수
    for x in range(i, i+3):
        for y in range(j, j+3):
             if a[x][y] == 0:
                a[x][y] = 1
             else:
                a[x][y] = 0
             
count = 0
if (n < 3 or m < 3) and a != b: # 리스트가 3x3보다 작다면 -1
    count = -1
else:
    for r in range(n-2): 
        for c in range(m-2):
             if a[r][c]!= b[r][c]:
                 count += 1
                 check(r, c)

if count != -1:
    if a != b:
       count = -1

print(count)