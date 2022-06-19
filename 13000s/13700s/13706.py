def binary_search(start, end):
    target = end
    while True:
        mid = (start + end) // 2 # 중간점
        if (mid ** 2) == target:
            return mid
        if mid ** 2 > target:
            end = mid
        elif mid ** 2 < target:
            start = mid

n = int(input())
print(binary_search(1, n))