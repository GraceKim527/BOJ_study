## 내 풀이

def solution(s):
    answer = []
    cnt = 0     
    zeroCnt = 0
    
    #"1"이 남을 때까지 반복
    while True:
        if s == "1":
            break
            
        zeroCnt += s.count("0")
        s = s.replace("0",'')
        s = bin(len(s))[2:]
        
        cnt += 1
        
    answer = [cnt, zeroCnt]    
    return answer

## 다른 사람의 풀이

def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]