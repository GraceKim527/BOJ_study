n = int(input()) # 마을의 수
v = list(map(int, input().split()))

max_v = max(v)
print(sum(v)- max_v)