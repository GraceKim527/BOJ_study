import sys 
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
ans = []

for i in range(n):
    ans.insert(i-numbers[i], i+1)

for k in ans:
    print(k, end=' ')