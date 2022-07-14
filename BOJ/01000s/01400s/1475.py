# 플라스틱 한 세트에 0 ~ 9
n = input()
lst = [0] * 10 # 10칸짜리 리스트
for i in n:
    chg = int(i)
    if chg == 9: # 9이면 6에다가 카운트 +1 해준다. (6이여도 상관 무)
        chg = 6
    lst[chg] += 1
lst[6] = (lst[6]+1) // 2 # n이 홀수인 경우에 한 세트를 더 사야함.
print(max(lst))