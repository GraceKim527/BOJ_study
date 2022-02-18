h, m = map(int, input().split())
n = int(input())

h += n // 60
m += n % 60

if m >= 60: #분이 60을 넘을 경우,
    h += 1
    m -= 60
if h >= 24: #시가 24를 넘을 경우,
    h -= 24

print(h, m)