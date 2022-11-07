import sys
input = sys.stdin.readline

n = int(input())

def count(n):
    count = 0
    while n != 0:
        n //= 5
        count += n
    return count

print(count(n))