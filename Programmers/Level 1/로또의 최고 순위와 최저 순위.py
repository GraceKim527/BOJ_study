## 내 풀이

def rank(r):
    if r == 6:
        return 1
    elif r == 5:
        return 2
    elif r == 4:
        return 3
    elif r == 3:
        return 4
    elif r == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    minimum = 0
    for l in lottos:
        if l in win_nums:
            minimum += 1
    maximum = minimum + lottos.count(0)
    
    answer = []
    answer.append(rank(maximum))
    answer.append(rank(minimum))
    return answer


## 다른 사람의 풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]