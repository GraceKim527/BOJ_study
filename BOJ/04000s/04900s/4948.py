def sosu(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True #소수 구하는 방식

limit_list = list(range(2, 246912))
memo = []

for i in limit_list: # 2부터 2,246,912 범위
    if sosu(i):
        memo.append(i) # 리스트 추가

n = int(input())

while True:
    count = 0 #갯수 세는 조건때문에 카운트
    if n == 0:
        break
    for i in memo: #memo리스트 중
        if n < i <= 2*n:
            count += 1 
    print(count)
    n = int(input()) #0 입력받기 전까지 계속 해야하므로 입력 받음