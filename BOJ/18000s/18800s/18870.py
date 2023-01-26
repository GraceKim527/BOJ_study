import sys
n = int(input())

nums = list(map(int, sys.stdin.readline().rstrip().split())) # 좌표 받기

numset = set(nums) # 중복 제거
a = list(numset) # 리스트로 만들고
a.sort() # 정렬

numdict = {} 
# 순서를 부여
for i in range(len(a)):
    numdict[a[i]] = i

for i in nums:
    print(numdict[i], end=' ')