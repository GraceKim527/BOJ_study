t = int(input()) # 테스트 케이스

for _ in range(t):
    money = int(input())
    dollars = [25, 10, 5, 1]
    for i in dollars:
        print(money // i, end = ' ')
        money = money % i 
    print()