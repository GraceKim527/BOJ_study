## 내 풀이

def solution(k, score):
    answer = []
    rank = []
    for s in score:
        rank.append(s)
        rank.sort(reverse=True)
        if len(rank) > k:
            answer.append(rank[k-1])
            rank.pop()
        else:
            answer.append(min(rank))
    return answer


## 다른 사람의 풀이
def solution(k, score):
    q = []
    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            ## 제일 작은 수만 remove해주면 됨.
            q.remove(min(q))
        answer.append(min(q))

    return answer