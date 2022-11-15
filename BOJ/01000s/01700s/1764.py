import sys 
input = sys.stdin.readline

N, M = map(int, input().split())

see = set()
hear = set()
for _ in range(N):
    see.add(input())
    
for _ in range(M):
    hear.add(input())

result = sorted(list(see & hear))

print(len(result))
for i in result:
    i = i.replace("\n", "")
    print(i)