import sys 
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
li = list(set(li))
li.sort()

for i in li:
    print(i, end=' ')