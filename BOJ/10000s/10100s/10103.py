n = int(input())
c_score = 100 # 창영
s_score = 100 # 상덕
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        s_score -= a
    elif a < b:
        c_score -= b
    else:
        continue
print(c_score)
print(s_score)