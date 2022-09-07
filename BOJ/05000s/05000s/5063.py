n = int(input()) # 테스트 케이스
for i in range(n):
    r, e, c = map(int, input().split())
    if r + c < e:
        print("advertise")
    elif r + c == e:
        print("does not matter")
    else:
        print("do not advertise")