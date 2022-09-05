t = int(input()) # 테스트 케이스

for i in range(t):
    a, b = map(int, input().split())
    a1, b1 = a, b
    while a!=0:
        b = b%a
        a, b = b, a

    gcd = b
    lcm = a1 * b1 // b
    print(lcm)