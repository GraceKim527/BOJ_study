import sys
input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())
apple_position = [int(input()) for _ in range(J)]

move = 0

start = 1
end = M

for i in range(J):
    if (end >= apple_position[i] and start <= apple_position[i]):
        continue
    elif (end < apple_position[i]):
        move += apple_position[i] - end
        end = apple_position[i]
        start = apple_position[i] - (M - 1)

    elif (start > apple_position[i]):
        move += start - apple_position[i]
        start = apple_position[i]
        end = apple_position[i] + (M - 1)

print(move)