# 2007년 1월 1일은 월요일

x, y = map(int, input().split()) #split()으로 나누어 받음. 1 1 
day = 0 # 얼마 지나는지(요일연산)
daylist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 1월부터 12월
weeklist = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'] # 일요일 ~ 토요일

for i in range(0, x - 1):
    day += daylist[i]
    
day = (day + y) % 7 # 요일 계산

print(weeklist[day])