import sys
input = sys.stdin.readline

N = int(input())
s = set()
ans = 0

for i in range(N):
    user = input().strip()
    if user == "ENTER":
        ans += len(s)
        s.clear()
    else:
        s.add(user)
ans += len(s)

print(ans)