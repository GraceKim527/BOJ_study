n = int(input()) # 점의 개수 
q1 = q2 = q3 = q4 = axis = 0
for i in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        q1 += 1
    elif x < 0 and y > 0:
        q2 += 1
    elif x < 0 and y < 0:
        q3 += 1
    elif x > 0 and y < 0:
        q4 += 1
    else:
        axis += 1
print("Q1: {}".format(q1))
print("Q2: {}".format(q2))
print("Q3: {}".format(q3))
print("Q4: {}".format(q4))
print("AXIS: {}".format(axis))