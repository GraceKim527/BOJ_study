i_e, i_s, i_m, cnt = 1, 1, 1, 1
e, s, m = map(int, input().split()) # 지구 E, 태양 S, 달 M

while True:
    if i_e == e and i_s == s and i_m == m:
        break
    i_e += 1
    i_s += 1
    i_m += 1
    cnt += 1
    if i_e >= 16:
        i_e -= 15
    if i_s >= 29:
        i_s -= 28
    if i_m >= 20:
        i_m -= 19

print(cnt)