import sys 
input = sys.stdin.readline

a, b = map(int, input().split())
m = int(input()) # 자리수의 개수

arr = list(map(int, input().split()))
arr.reverse() # 첫째자리부터 계산

ten = 0
for i in range(m):
  ten += arr[i]*(a**i)
  
result = []

while ten // b: # 몫이 0
  result.append(ten % b)
  ten = ten // b

result.append(ten)

result.reverse()
print(' '.join(map(str, result)))