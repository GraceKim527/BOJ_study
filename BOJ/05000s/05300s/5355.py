t = int(input()) #테스트 케이스
for i in range(t):
    mars = list(map(str, input().split()))
    result = 0 
    for i in range(len(mars)):
        if i == 0:
            result += float(mars[i])
        else:
            if mars[i] == '#':
                result -= 7
            elif mars[i] == '%':
                result += 5
            elif mars[i] == '@':
                result *= 3
    print("%0.2f" % result)