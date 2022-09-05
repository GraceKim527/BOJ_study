a = input()
b = input()
cnt = 0
n = 0
while n <= len(a) - len(b):
    if a[n:n + len(b)] == b:
        cnt += 1
        n += len(b) # 단어 길이만큼 인덱스를 더해준다.
    else:
        n += 1 # 1만큼 인덱스를 더한다.

print(cnt)