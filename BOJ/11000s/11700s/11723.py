import sys
input = sys.stdin.readline

M = int(input()) # 연산의 수
s = set()
for _ in range(M):
    temp = input().strip().split()
    
    if len(temp) == 1:
        if temp[0] == 'all':
            s = set((i for i in range(1, 21)))
        else:
            s = set()
    
    else:
        cmd, num = temp[0], temp[1]
        num = int(num)

        if cmd == 'add':
            s.add(num)
        elif cmd == 'remove':
            s.discard(num)
        elif cmd == 'check':
            print(1 if num in s else 0)
        elif cmd == 'toggle':
            if num in s:
                s.discard(num)
            else:
                s.add(num)