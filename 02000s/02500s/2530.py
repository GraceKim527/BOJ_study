h, m, s = map(int, input().split()) # 시, 분, 초
time = int(input())
s += time
m += s//60
h += m//60
print(h%24, m%60, s%60)