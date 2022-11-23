import sys
input = sys.stdin.readline

bar = list(input())
stack = []
cnt = 0

for i in range(len(bar)-1):
    if bar[i] == '(':
        stack.append('(')
    else: # ')'이면,
        if bar[i - 1] == '(': # 그 전꺼가 '(' 이라는 것은 레이저를 의미
            stack.pop()
            cnt += len(stack) # 레이저로 인해 막대기가 끊어졌으니 기존 stack의 길이를 모두 구함.

        else:
            stack.pop()
            cnt += 1

print(cnt)