s = input().split('-')
num = []
for i in s:
    sum = 0
    tmp = i.split('+') 
    for j in tmp:
        sum += int(j)
    num.append(sum)

n = num[0] # 0번째 값에서 나머지 값들을 빼준다.
for i in range(1, len(num)):
    n -= num[i]
print(n)