tree = int(input()) #묘목 갯수
day = list(map(int, input().split())) # 며칠이 걸리는지를 나타냄

day.sort(reverse=True) #다 자라는데 걸리는 일수가 높은 순으로 나무를 심음 

for i in range(tree):
    day[i] = day[i] + i + 1 #1일부터 시작하기 때문에 1을 더함

print(max(day) + 1) 