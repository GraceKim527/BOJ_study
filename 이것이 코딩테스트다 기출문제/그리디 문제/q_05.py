import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ball = list(map(int, input().split())) # 볼링공 정보

arr = [0] * 11

result = 0

for b in ball:
    arr[b] += 1

for i in range(1, m+1):
    n -= arr[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수 제외)
    result += arr[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)