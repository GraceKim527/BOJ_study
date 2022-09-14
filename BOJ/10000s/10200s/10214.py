from re import L


t = int(input()) # 테스트 케이스
for i in range(t):
    y = k = 0
    for _ in range(9):
        y_score, k_score = map(int, input().split())
        y += y_score
        k += k_score

    if y > k:
        print("Yonsei")
    elif k > y:
        print("Korea")
    else:
        print("Draw")