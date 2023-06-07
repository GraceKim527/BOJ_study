## 내 풀이
from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    flag = True
    for word in goal:
        if cards1 and word == cards1[0]:
            cards1.popleft()
            continue
            
        if cards2 and word == cards2[0]: 
            cards2.popleft()
            continue
        flag = False
        break
    if flag == True:
        answer = 'Yes'
    else:
        answer = 'No'
    return answer

## 다른 사람의 풀이
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
