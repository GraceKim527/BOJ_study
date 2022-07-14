n = int(input())
numbers = map(int, input().split())
so = 0
for num in numbers: # 1 3 5 7
    error = 0
    if num > 1:
        for i in range(2, num): #2부터 num-1
            if num % i == 0: #몫이 0이면 error
                error += 1 
        if error == 0: 
            so += 1 #에러가 없으면 소수
print(so)