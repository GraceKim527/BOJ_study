import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n은 날짜 수 k는 연속적인 날짜 수
tem = list(map(int, input().split())) 
continuous_temp = []
continuous_temp.append(sum(tem[:k]))

for i in range(n - k):
    continuous_temp.append(continuous_temp[i] - tem[i] + tem[i+k])

print(max(continuous_temp))