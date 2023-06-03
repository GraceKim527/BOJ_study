## 내 풀이

def solution(num):
    cnt = 0
    if num == 1:
        return 0
    
    while True:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        cnt += 1
        
        if num == 1:
            return cnt 
        elif cnt == 500:
            return -1
    
    return cnt

## 다른 사람의 풀이

def collatz(num):
    for i in range(500):
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    return -1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(78))