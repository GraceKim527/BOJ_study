n = int(input())
cnt = 1
pileup = 1
while n > pileup:
    pileup += 6 * cnt
    cnt += 1 #반복문 반복 휫수

print(cnt)