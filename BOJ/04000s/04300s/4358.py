import sys
input = sys.stdin.readline

total = 0
dic = dict()
while True:
    word = input().rstrip()
    if word == '':
        break
    total += 1
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

sdic = dict(sorted(dic.items()))
for i in sdic:
    a = sdic[i]
    per = (a / total * 100)

    print("%s %.4f" %(i, per))