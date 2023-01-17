import sys
input = sys.stdin.readline

data = input()

# 모두를 0으로 바뀔 때 쓰는 휫수
count0 = 0
# 모두를 1로 바꿀 때 쓰는 휫수
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        # 다음 수에서 1로 바뀐다면
        if data[i+1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀐다면
        else:
            count1 +=1

print(min(count0, count1))