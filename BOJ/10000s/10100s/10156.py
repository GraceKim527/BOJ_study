k, n, m = map(int, input().split()) # 과자 한 개 가격, 사려고 하는 과자 갯수, 가진 돈
total = k * n - m
if total < 0:
    print("0")
else:
    print(total)