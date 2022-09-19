n = int(input())
divisor = list(map(int, input().split()))
n_max = max(divisor)
n_min = min(divisor)

print(n_max * n_min)