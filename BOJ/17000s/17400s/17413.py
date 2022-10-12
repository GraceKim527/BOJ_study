import sys
s = list(map(str, sys.stdin.readline().rstrip()))
result = ""
word = ""
reverse = True # 단어 거꾸로

for s in s: # <open>tag<close>
    if s == '<':
        reverse = False
        result += word
        word = s
    elif s == '>':
        reverse = True
        result += (word + '>')
        word = ""
    elif s == ' ':
        result += word + s
        word = ""
    elif reverse:
        word = s + word
    else:
        word += s
    
result += word
print(result)