
# str_li = []
# for _ in range(N):
#     str_li.append(input().rstrip())

# count = 0
# for _ in range(M):
#     string = input().rstrip()
#     for i in str_li:
#         if i == string:
#             count += 1

# print(count)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s1 = [input().rstrip() for _ in range(N)]
s2 = [input().rstrip() for _ in range(M)]

cnt = 0
for str in s2:
    if str in s1:
        cnt += 1

print(cnt)