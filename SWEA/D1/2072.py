import sys 
input = sys.stdin.readline

T = int(input())
for t in range(T):
    li = list(map(int, input().split()))
    sum = 0
    for i in li:
        if i % 2 == 1:
            sum += i
    print("#{} {}".format(t+1, sum))