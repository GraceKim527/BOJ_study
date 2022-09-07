bowl = list(input()) #리스트형으로 받는다.
result = 0
for i in range(len(bowl)):
    if i == 0:
        result += 10
    elif bowl[i] == bowl[i - 1]:
        result += 5
    else:
        result += 10
    
print(result)