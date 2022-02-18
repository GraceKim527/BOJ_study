def fun():
    check = [False, False] + [True] * 10000
    for i in range(2, 101):
        if check[i] == True:
            for j in range(i + i, 10001, i):
                check[j] = False #소수가 아닌 것들을 False로 바꾼다.
    
    t = int(input())
    for _ in range(t):
        n = int(input())

        a = n // 2
        b = a
        for _ in range(10000):
            if check[a] and check[b]: #a와 b가 모두 소수가 아니라면, 값을 바꿔서 탐색.
                print(a,b)
                break
            a -= 1
            b += 1

fun()