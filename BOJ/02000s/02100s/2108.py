# counter
from collections import Counter
import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(li)/n))

# 중앙값
li.sort()
print(li[n//2])

# 최빈값
temp = Counter(li).most_common()
if len(li) > 1:
    if temp[0][1] == temp[1][1]:
        print(temp[1][0])
    else:
        print(temp[0][0])
else:
    print(temp[0][0])

# 최댓값과 최솟값 차이
print(max(li) - min(li))