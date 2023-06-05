## 나의 풀이
def solution(nums):
    unique_types = len(set(nums))

    if len(nums) / 2 > unique_types:
        return unique_types
    else:
        return len(nums) / 2
    
## 다른 사람의 풀이
def solution(nums):
    return min(len(set(nums)), len(nums)//2)