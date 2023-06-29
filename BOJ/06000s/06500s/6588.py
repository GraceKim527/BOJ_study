import sys
input = sys.stdin.readline

r = 1000000
check = [True for _ in range(r)]
for i in range(2, int(r ** 0.5)):
    if check[i] == True:
        for j in range(i * 2, r, i): 
            if check[j] == True:
                check[j] = False

while(True):
    n = int(input())
    if n == 0: 
        break
    for i in range(3, r, 2): #홀수부터 시작, 홀수만 체크안하고 짝수까지 체크하게 되면 시간 초과가 발생
        if check[i] == True:
            if check[n - i] == True:
                print("%d = %d + %d" % (n , i , n - i))
                break