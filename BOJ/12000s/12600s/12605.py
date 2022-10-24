import sys

input = sys.stdin.readline
n = int(input())

for i in range(1, n+1):
    word = list(input().rstrip().split())

    print("Case #%d: %s" % (i, " ".join(word[::-1])))