import sys
input = sys.stdin.readline

# N은 단어의 개수, M은 외울 단어의 길이 기준
N, M = map(int, input().split()) # N = 7, M = 4

words = {}

# 1. 자주 나오는 단어일수록
# 2. 해당 단어의 길이가 길수록
# 3. 알파벳 사전 순으로 앞 단어일수록
for _ in range(N):
  word = input().rstrip()
  
  if len(word) < M: # 단어가 M미만일 경우 아예 데이터를 검사하지 않게끔.
    continue
  else: 
    if word in words: 
      words[word] += 1
    else: 
      words[word] = 1

# 빈도수가 높은 순서로 내림차순, 단어의 길이가 짧은 순서로 내림차순, 알파벳 순서로 오름차순.
words = sorted(words.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for word in words:
  print(word[0])