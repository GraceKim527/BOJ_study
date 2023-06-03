## 내 풀이

from itertools import combinations

def solution(numbers):
    answer = set()
    for i in list(combinations(numbers, 2)):
        answer.add(sum(i))
    return sorted(answer)

## 다른 사람의 풀이도 유사해서 생략