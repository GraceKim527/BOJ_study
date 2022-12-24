import sys
input = sys.stdin.readline 

n, m = map(int, input().split()) # 카드의 개수, 카드 합체를 몇 번 하는지
card = list(map(int, input().split())) 

for _ in range(m):
    card.sort()
    card[0] = card[1] = card[0] + card[1]

print(sum(card))