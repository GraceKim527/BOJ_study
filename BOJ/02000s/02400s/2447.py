def def_star(n):
    mar = []
    for i in range(3 * len(n)):
        #n이 3으로 나누어 떨어지지 않는다면, 가운데 공백
        if i // len(n) == 1:
            mar.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        
        #n이 3으로 나누어 떨어지면, 공백 없이 다 채운다.
        else:
            mar.append(n[i % len(n)] * 3)
    return mar

star = ["***", "* *", "***"]
n = int(input())

r = 0
#만약 n이 3이 될때 까지 n은 3으로 나눠준 값을 다시 n값으로 지정하고 1씩 추가
while n != 3:
    n = int(n/3)
    r += 1
    #r은 함수를 몇 번 실행할지 정하는 변수
for i in range(r):
    star = def_star(star)
for i in star:
    print(i)