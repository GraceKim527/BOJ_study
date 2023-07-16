import sys 
from math import gcd
input = sys.stdin.readline

N = int(input())

first = int(input())
tree = []

# 간격 저장
for i in range(N-1):
    num = int(input())
    tree.append(num - first)
    first = num
    
g = tree[0]
for j in range(1, len(tree)):
    g = gcd(g, tree[j])

# 가로수 개수 : 간격 // 최대공약수 - 1
result = 0
for each in tree:
    result += each // g - 1
print(result)