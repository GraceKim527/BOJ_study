jin = input() # 진호의 mbti
n = int(input()) # 친구들 수

fr = []
for _ in range(n):
    fr.append(input()) # mbti 넣기

cnt = 0
for i in fr:
    if i == jin:
        cnt += 1
    
print(cnt)