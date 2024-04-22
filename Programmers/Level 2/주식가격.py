from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []

    # 큐를 사용한다면 추가적인 인덱싱 없이 더 간편하게 구현이 가능할 것 같아서 큐도 활용하였다. prices로 queue를 초기화 시킨 후에 반복문을 돌면서 앞에서부터 하나씩 popleft해서 popleft한 뒤의, 남은 queue를 순회하며 값이 작아지기 전까지 초를 증가시키는 것을 queue가 빌때까지 반복하면 된다.
    while queue:
        price = queue.popleft()
        sec = 0
        # '초'
        for q in queue:
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer