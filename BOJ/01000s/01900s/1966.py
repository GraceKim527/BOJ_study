import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split()) # N은 문서의 개수, 찾으려는 정수가 몇 번째 큐에 담겨 있는지
    queue = deque(map(int, input().split())) # 큐의 중요도대로
    
    count = 0
    while queue:
        best = max(queue)
        front = queue.popleft()
        m -= 1

        if best == front:
            count += 1
            if m < 0:
                print(count)
                break

        else:
            queue.append(front)
            if m < 0:
                m = len(queue) - 1