import sys

input = sys.stdin.readline

# n은 포켓몬 개수, m은 맞추어야 할 문제
n, m = map(int, input().split())
poke_book = {}

for i in range(1, n+1):
    poke = input().rstrip() # \n 삭제
    poke_book[i] = poke
    poke_book[poke] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(poke_book[int(quest)])
    else:
        print(poke_book[quest])
