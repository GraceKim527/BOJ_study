m = int(input())
n = int(input())
sosu_list = []
for num in range(m, n+1): #60 100
    error = 0 #error값을 초기화
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1 #error 값을 분별하기 위한 코드 
                break
        if error == 0:
            sosu_list.append(num)

if len(sosu_list) > 0:
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)