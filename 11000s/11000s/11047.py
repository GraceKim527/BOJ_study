n, k = map(int, input().split()) #n은 종류, k는 가치의 합

# for문을 이용해 카운트 해주고, 나머지 동전을 내림차순, 우선 가치에 맞는 큰 수를 찾아야 함.
count = 0
coin = list()
for i in range(n):
    coin.append(int(input()))

for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if coin[i] > k:
        continue
    count += k//coin[i]
    k %= coin[i]

print(count)