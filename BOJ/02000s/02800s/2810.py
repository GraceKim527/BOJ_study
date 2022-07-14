n = int(input()) # 좌석의 수
seet = input()

love = seet.count('LL') # 커플석 몇 개인지 
if love <= 1: # 커플석 1개 혹은 없다면,
    print(len(seet)) # seet 그대로 출력, 커플석에는 거치대가 x
else:
    print(len(seet) - love + 1) # 마지막 + 1은 끝에 컵홀더 더 있는거