import sys 
input = sys.stdin.readline

T = int(input()) # 테스트 케이스

for _ in range(T):
    a, b = map(int, input().split()) 

    test = a % 10
    
    if test == 0:
        print(10)
    elif test in [1,5,6]:
        print(test)
    elif test in [4, 9]:
        test2 = b % 2
        if test2 == 0:
            print(test*test%10)
        else:
            print(test)

    else:
        test2 = b % 4
        if test2 == 0:
            print(test**4%10)
        else:
            print(test**test2%10)