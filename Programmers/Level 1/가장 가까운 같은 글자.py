def solution(s):
    answer = []
    word_dict = dict()
    
    for i, word in enumerate(list(s)):
        if word not in word_dict:
            answer.append(-1)
            word_dict[word] = i
        else:
            answer.append(i-word_dict[word])
            word_dict[word] = i
    return answer