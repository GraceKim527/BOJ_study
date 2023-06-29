def solution(survey, choices):
    scores = [0] * 8
    dic = {'R': 0, 'T': 1, 'C': 2, 'F': 3, 'J': 4, 'M': 5, 'A': 6, 'N': 7}

    # 점수 +
    for i in range(len(survey)):
        score = choices[i] - 4 # 4를 빼면 문제와 같이 -3, -2, -1, 0, 1, 2, 3 이 되기 때문
        if score < 0:
            scores[dic[survey[i][0]]] -= score
        elif score > 0:
            scores[dic[survey[i][1]]] += score

    # 검사 결과
    # 점수가 같으면 사전순으로 앞서는 문자를 저장해야 한다.
    answer = ''
    answer += 'T' if scores[0] < scores[1] else 'R'
    answer += 'F' if scores[2] < scores[3] else 'C'
    answer += 'M' if scores[4] < scores[5] else 'J'
    answer += 'N' if scores[6] < scores[7] else 'A'
    return answer