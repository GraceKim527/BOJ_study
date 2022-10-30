import sys
input = sys.stdin.readline

# N명의 사람, K는 K번째 사람 제거
n, k = map(int, input().split())

ans = []
array = [i for i in range(1, n+1)]
num = 0
for i in range(n):
    num += (k - 1)
    if num >= len(array):
        num %= len(array)
    ans.append(str(array[num]))
    array.pop(num)

print("<", ", ".join(ans), ">", sep="")