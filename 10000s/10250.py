test = int(input()) #테스트 데이터
for i in range(test):
    h, w, n = map(int, input().split()) #h = 층, w = 방 갯수
    num = n//h + 1
    floor = n % h
    if n % h == 0:
        num = n//h
        floor = h
    print(f'{floor*100+num}')
