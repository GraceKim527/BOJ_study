n = int(input()) # 우유 가게 수 
# 딸기 -> 초코 -> 바나나 -> 딸기
# 0 딸기 1 초코 2 바나나
milk = list(map(int, input().split())) # list형태로 우유 순서 저장

count = 0
for i in range(n):
    if milk[i] == count % 3: # 3으로 나누었을 때 나머지와 같으면 count += 1
        count += 1

print(count)