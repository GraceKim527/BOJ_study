import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n은 저장된 사이트 주소, m은 비밀번호를 찾으려는 사이트 주소의 수

pw = {}
for _ in range(n):
    web, ps = input().split()
    pw[web] = ps

for _ in range(m):
    print(pw[input().rstrip()])