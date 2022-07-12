s = int(input()) # 자연수의 합
n = 0 # 최댓값
result = 0

for i in range(1, s+1):
    result += i
    n += 1
    if (result > s): # 자연수의 합보다 커질 경우엔 프로그램 종료
        n -= 1
        break
print(n)