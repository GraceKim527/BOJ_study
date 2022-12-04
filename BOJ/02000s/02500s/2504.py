import sys
input = sys.stdin.readline

string = input().rstrip()

stack = []
temp = 1
result = 0

for i in range(len(string)):
    if string[i] == '(':
        temp *= 2
        stack.append(string[i])
    elif string[i] == '[':
        temp *= 3
        stack.append(string[i])
    elif string[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if string[i-1] == '(':
            result += temp
        temp //= 2
        stack.pop()
    else: # ']'
        if not stack or stack[-1] == '(':
            result = 0
            break
        if string[i-1] == '[':
            result += temp
        temp //= 3
        stack.pop()

if stack:
    result = 0 
print(result)