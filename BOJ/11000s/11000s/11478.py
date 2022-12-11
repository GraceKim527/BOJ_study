import sys
input = sys.stdin.readline

s = input().rstrip()
total = set()
for i in range(len(s)):
    for j in range(len(s)):
        total.add(s[i:j+1]) #i번째 문자부터 부분문자열 구하기

print(len(total)-1)