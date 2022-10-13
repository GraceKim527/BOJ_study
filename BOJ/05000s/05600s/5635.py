li = []
for _ in range(int(input())):
    name, d, m, y = input().split()
    li.append([name, int(d), int(m), int(y)])

li.sort(key = lambda x:(x[3], x[2], x[1])) # 년, 월, 일 순으로 정렬

print(li[-1][0])
print(li[0][0])