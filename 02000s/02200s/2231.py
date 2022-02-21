n = int(input()) #216 + 2+ 1+ 6 = 225

for i in range(1, n+1):
    num = sum((map(int, str(i)))) #i의 각자리 수를 더함
    num_sum = i + num #생성자 + 각자릿수 합 
    if num_sum == n:
        print(i)
        break
    if i == n:
        print(0)