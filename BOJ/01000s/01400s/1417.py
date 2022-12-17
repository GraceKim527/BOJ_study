import sys
input = sys.stdin.readline

n = int(input())
vote = []
ans = 0

for _ in range(n):
    vote.append(int(input()))

m = max(vote)


while m != vote[0] or vote.count(m)>=2:
    maxIdx = vote[1:].index(max(vote[1:]))+1
    vote[0] += 1
    vote[maxIdx] -= 1
    ans += 1
    m = max(vote)

print(ans)