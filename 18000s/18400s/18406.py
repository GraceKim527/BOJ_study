num = input() # int형 말고 문자열로 받자.
a = 0 # 가운데를 기준으로 왼쪽
b = 0 # 가운데를 기준으로 오른쪽

# 예외처리
if len(num) % 2 == 0: 
    for i in range(0, len(num) // 2): # 절반 계산
        a += int(num[i])
    for i in range(len(num) // 2, len(num)): # 남은 절반 계산
        b += int(num[i])
else:
    print("입력으로 홀수 형태는 받지 않습니다.")

if a == b:
    print("LUCKY")
else:
    print("READY")