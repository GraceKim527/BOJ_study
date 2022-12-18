import sys
input = sys.stdin.readline

N = int(input())

dic = {}
for _ in range(N):
    card = int(input())
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1

# 카드값 : 카드개수
result = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])