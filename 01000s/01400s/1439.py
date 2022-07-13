s = input() # 문자열
count = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]: # 0과 1이 다를 경우 바꾸기 때문에, 같지 않으면 count해주면 된다.
        count += 1

print((count+1)//2)