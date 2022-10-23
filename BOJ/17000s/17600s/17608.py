import sys 
input = sys.stdin.readline

n = int(input())

h = []
for _ in range(n):
    h.append(int(input()))

count = 1
pop = h[-1]
for _ in range(len(h)):
    temp = h.pop()
    if pop < temp:
        pop = temp
        count += 1

print(count)