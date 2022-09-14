v = int(input()) # 심사위원 수
vote = list(input()) # 투표 수
a = b = 0
for i in vote:
    if i == 'A':
        a += 1
    else:
        b += 1
if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("Tie")