import sys
input = sys.stdin.readline

word_l = list(input().rstrip())
word_r = []
n = int(input())

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'L' and word_l:
        word_r.append(word_l.pop())
    
    elif cmd[0] == 'D' and word_r:
        word_l.append(word_r.pop())
    
    elif cmd[0] == 'B' and word_l:
        word_l.pop()
    elif cmd[0] == 'P':
        word_l.append(cmd[1])

print("".join(word_l + list(reversed(word_r))))