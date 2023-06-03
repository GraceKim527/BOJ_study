## 내 풀이
def solution(name, yearning, photo):
    person_dict = {}
    answer = []
    for i in range(len(name)):
        person_dict[name[i]] = yearning[i]
        
    for i in range(len(photo)):
        misspoint = 0
        for j in photo[i]:
            
            if j in person_dict.keys():
                misspoint += person_dict[j]
        answer.append(misspoint)
            
    return answer

## 다른 사람의 풀이
def solution(name, yearning, photo):
    dictionary = dict(zip(name,yearning))
    scores = []
    for pt in photo:
        score = 0
        for p in pt:
            if p in dictionary:
                score += dictionary[p]
        scores.append(score)
    return scores

## 나와 유사하지만 여기서 zip() 메서드를 사용해서 데이터를 묶었다. 