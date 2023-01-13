import sys 
input = sys.stdin.readline

k = int(input())

a = [1]
b = [0]

for i in range(k):
    a.append(b[i])
    b.append(a[i] + b[i])

print(a[-1], end=" ")
print(b[-1])