import sys 
input = sys.stdin.readline

N = int(input())
time = []
money = []
dp = []
for i in range(N):
    a, b = map(int, input().split())
    time.append(a)
    money.append(b)
    dp.append(b)
dp.append(0)
for i in range(N-1, -1, -1):
    if time[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], money[i] + dp[i + time[i]])
print(dp[0])