import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    l = input().rstrip()
    word_l = []
    word_r = []

    for i in l:
        if i == '<':
            if word_l:
                word_r.append(word_l.pop())

        elif i == '>':
            if word_r:
                word_l.append(word_r.pop())

        elif i == '-':
            if word_l:
                word_l.pop()

        else:
            word_l.append(i)
    print("".join(word_l + list(reversed(word_r))))