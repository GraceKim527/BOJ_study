import sys
input = sys.stdin.readline

score = [int(input()) for _ in range(8)]

score_sort = sorted(score, reverse=True)
high = []
for i in range(5):
    high.append(score_sort[i])

tmp = []
for i in high:
    tmp.append(score.index(i))

print(sum(high))
tmp_s = sorted(tmp)
for i in tmp_s:
    print(i + 1, end=" ")