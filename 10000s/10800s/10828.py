import sys #sys.stdin.readline을 사용하기 위해 import
count = int(sys.stdin.readline()) #input()보다 빠른 속도로 입출력이 가능하다.

stack = []
for _ in range(count):
    command = sys.stdin.readline().split() #리스트로 저장
    
    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop()) #공백일 경우 맨 마지막 요소를 빼기 때문에 공백으로 남겨둬도 괜찮다.
    
    elif command[0] == 'size':
        print(len(stack))
    
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])