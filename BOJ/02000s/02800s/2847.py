import sys
input = sys.stdin.readline

N = int(input()) # 레벨의 수
score = []
for _ in range(N):
    score.append(int(input())) # 클리어했을 때 얻는 점수들
    
count = 0
for i in range(N-2, -1, -1): # 뒤에서부터 확인
    if score[i] >= score[i+1]: # 
        count += score[i] - score[i+1] + 1
        score[i] = score[i+1]-1 # 다음 값보다는 작게 만들어야 함.

print(count)