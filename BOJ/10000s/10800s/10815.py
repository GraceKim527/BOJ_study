import sys

input = sys.stdin.readline
n = int(input()) # 카드 갯수
card = list(map(int, input().split()))
m = int(input()) # 찾는 갯수
check = list(map(int, input().split()))

card.sort()
answer = []
def binary_search(k, card, start, end):
    mid = (start + end) // 2
    if start > end:
        answer.append(str(0))
    elif k == card[mid]:
        answer.append(str(1))
    elif k > card[mid]:
        binary_search(k, card, mid+1, end)
    else:
        binary_search(k, card, start, mid-1)

for k in check:
    start = 0
    end = len(card) - 1
    binary_search(k, card, start, end)

print(' '.join(answer))