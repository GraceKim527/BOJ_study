import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    str = input().rstrip()
    words = list(str.split())
    reverse_words = []

    for word in words:
        reverse_words.append(word[::-1])
    
    ans = " ".join(reverse_words)
    print(ans)