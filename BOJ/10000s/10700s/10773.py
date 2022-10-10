import sys
input = sys.stdin.readline

li = []
for i in range(int(input())):
    st = int(input())
    if st == 0:
        li.pop()
        continue
    li.append(st)

sum = 0
for i in li:
    sum += i
print(sum)