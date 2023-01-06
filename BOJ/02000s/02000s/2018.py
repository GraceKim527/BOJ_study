import sys 
input = sys.stdin.readline

n = int(input())
start, end = 1, 1
count, total = 0, 1

while end != n:
    if total < n:
        end += 1
        total += end
    elif total > n :
        total -= start
        start += 1
    else:
        count += 1
        end += 1
        total += end

print(count + 1)