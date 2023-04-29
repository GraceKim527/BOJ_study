import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n은 나무의 수, m은 가져갈 나무의 길이
tree = list(map(int, input().split()))

start, end = 1, max(tree) # 이분탐색

while start <= end:
    mid = (start + end) // 2

    log = 0 # 벌목된 나무의 현재 상태
    for i in tree:
        if i >= mid:
            log += i - mid

        # 벌목 높이를 이분탐색
    if log >= m: # 수가 올라가면 벌목되는 나무 수가 적어짐.
        start = mid + 1
    else: 
        end = mid - 1

print(end)