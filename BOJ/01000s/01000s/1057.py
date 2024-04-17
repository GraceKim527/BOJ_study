import sys 
input = sys.stdin.readline

N, Jimin, Hansu = map(int, input().split()) # 참가자 수, 김지민 번호, 임한수 번호
count = 0

while Jimin!=Hansu:
    Jimin -= Jimin // 2 # 자연수 몫만
    Hansu -= Hansu // 2 # 자연수 몫만
    count += 1

print(count)