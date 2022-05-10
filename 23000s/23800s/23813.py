n = list(input())
total = 0
for i in range(len(n)): # n의 길이만큼
    n.insert(0, n[-1])
    del n[-1]
    total += int("".join(n)) #리스트라서 바로 넣어줄 수가 없음. 
    #join을 이용해서 문자열을 풀어주고, int형으로 더해줌
    
print(total)