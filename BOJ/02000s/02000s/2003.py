import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right <= N and left <= right:
    sum_nums = nums[left:right] # 슬라이싱으로 구역나누기
    total = sum(sum_nums)
    if total == M:
        cnt += 1 # 경우의수 추가
        right += 1
    elif total < M:
        right += 1
    else:
        left += 1

print(cnt)