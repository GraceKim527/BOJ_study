import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
n_list = list(map(int, input().split()))

for i in range(N-1):
    n_list[i+1] += n_list[i]
n_list = [0] + n_list

for _ in range(M):
    a, b = map(int, input().split())
    print(n_list[b] - n_list[a-1])
