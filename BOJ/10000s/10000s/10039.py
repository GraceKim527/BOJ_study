sum = 0 # 5명 점수 합
for i in range(5):
    x = int(input())
    if x < 40:
        sum += 40
    else:
        sum += x
print(int(sum / 5)) #정수로 출력