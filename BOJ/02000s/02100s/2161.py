n = int(input()) # 정수
card_list = [i for i in range(1, n+1)]
discard = []

while len(card_list) != 1:
    discard.append(card_list.pop(0)) # 버리기
    card_list.append(card_list.pop(0)) # 뒤로 옮기기

for i in discard:
    print(i, end = ' ')

print(card_list[0])