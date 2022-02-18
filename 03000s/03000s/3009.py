x_n = []
y_n = []
for _ in range(3):
    x, y = map(int, input().split())
    x_n.append(x)
    y_n.append(y)

for i in range(3):
    if x_n.count(x_n[i]) == 1:
        x4 = x_n[i]
    if y_n.count(y_n[i]) == 1:
        y4 = y_n[i]
print(x4, y4)