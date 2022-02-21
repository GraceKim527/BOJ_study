t = int(input())
xy_list = []
for i in range(t):
    x, y = map(int, input().split()) #x는 몸무게, y는 키
    xy_list.append((x,y))

for i in xy_list: # 55, 185
    rank = 1
    for j in xy_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")