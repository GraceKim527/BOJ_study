## 내 풀이
from itertools import combinations
def is_prime_number(num):
    if num == 0 or num == 1: # 0과 1은 소수가 아님. 
        return False
    else:
        for n in range(2, (num // 2) + 1): # 소수판별
            if num % n == 0:
                return False
        return True

def solution(nums):
    answer = 0
    num_list = list(combinations(nums, 3))
    for arr in num_list:
        if is_prime_number(sum(arr)):
            answer += 1 
    return answer

## 다른 사람의 풀이
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer