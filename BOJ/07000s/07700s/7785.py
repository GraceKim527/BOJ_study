import sys
input = sys.stdin.readline

n = int(input())
com = dict()

for _ in range(n):
    name, con = map(str, input().split())

    if con == 'enter':
        com[name] = con
    else:
        del com[name]

for co in sorted(com, reverse=True):
    print(co)