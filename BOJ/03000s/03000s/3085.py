import sys 
input = sys.stdin.readline

def count():
    global maxi
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if data[i][j] == data[i][j-1]:
                cnt += 1
                maxi = max(maxi, cnt)
            else:
                cnt = 1
        cnt = 1
        for j in range(1, n):
            if data[j][i] == data[j-1][i]:
                cnt += 1
                maxi = max(maxi, cnt)
            else:
                cnt = 1

n = int(input()) # 개수 
data = [list(input()) for _ in range(n)]
maxi = 0

for i in range(n):
    for j in range(n):  
        # 열
        if j+1 < n:
            # 인접한 것 바꾸기
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
            count()
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]

        # 행
        if i+1 < n:
            data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
            count()
            data[i][j], data[i+1][j] = data[i+1][j], data[i][j]

print(maxi)