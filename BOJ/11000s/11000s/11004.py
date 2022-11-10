import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A_list = list(map(int, input().split()))

A_list.sort()
print(A_list[K-1])