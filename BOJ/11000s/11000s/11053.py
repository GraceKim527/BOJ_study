import sys 
input = sys.stdin.readline

n = int(input()) # 수열의 크기 
a = list(map(int, input().split())) # 10 20 10 30 20 50

dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]

    dp[i] += 1

print(max(dp))