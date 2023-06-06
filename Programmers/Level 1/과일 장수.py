## 내 풀이
def solution(k, m, score):
    score.sort(reverse=True) # 내림차순
    score_list = []
    answer = 0
    tmp = 0
    for _ in range(len(score)//m): # 슬라이싱 해야하는 휫수
        score_list.append(score[tmp:tmp+m])
        tmp += m
    for i in range(len(score_list)):
        answer += min(score_list[i]) * m

    return answer

## 다른 사람의 풀이 1
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m

## 다른 사람의 풀이 2

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    apple_box = []
    for i in range(0, len(score), m):
        apple_box.append(score[i:i+m])
    for apple in apple_box:
        if len(apple) == m: # 이렇게 리스트의 길이를 검사해서 answer에 한 번 더 옮겨주는 방식의 코드.
            answer += min(apple) * m

    return answer