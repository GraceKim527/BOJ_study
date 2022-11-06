import sys
input = sys.stdin.readline

for i in range(3):
    yut = list(map(int, input().split()))
    count = yut.count(1)
    # 1은 등

    if count == 3:
        print('A')
    elif count == 2:
        print('B')
    elif count == 1:
        print('C')
    elif count == 0:
        print('D')
    else:
        print('E')
