## 내 풀이

def solution(number, limit, power):
    div = [1] # 1의 약수는 무조건 1
    for i in range(2, number+1):
        cnt = 0
        for j in range(1, int(i**(1/2)+1)): #제곱근까지만 범위 설정
            if i % j == 0:
                cnt += 1
                if j**2 != i: #제곱이 되는 약수 중복 방지
                    cnt += 1
        if cnt > limit:
            cnt = power
            div.append(cnt)
        else:    
            div.append(cnt)
    return sum(div)

## 제곱근이 아닌 전체 범위로 설정했을 때 시간 초과가 많이 떴다. 

## 다른 사람의 풀이

def cf(n): # 공약수 출력
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))
def solution(number, limit, power):
    return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])