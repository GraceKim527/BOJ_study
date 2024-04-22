def solution(progresses, speeds):
    answer = []
    # 작업 리스트가 빌 때까지 반복
    while progresses:
        # 몇개의 기능이 배포되는지 저장 
        cnt = 0
        
        # 만약 맨 앞이 100%을 넘었다면, progresses와 speeds의 해당 값들을 없애주고, 카운트.
        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
            
        # 작업 진행도 추가
        progresses = [progresses[i]+speeds[i] for i in range(len(progresses))]

        # 만약 오늘 기능이 배포되었다면 결과리스트에 추가
        if cnt:
            answer.append(cnt)
    
    return answer