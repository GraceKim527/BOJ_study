import sys 
input = sys.stdin.readline

n = int(input()) # 카드 갯수
card = list(map(int, input().split()))
m = int(input()) # 찾는 갯수
check = list(map(int, input().split()))

dic = dict()

for i in card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
for i in range(m):
    if check[i] in dic:
        print(dic[check[i]], end=' ')
    else:
        print(0, end=' ')