n = int(input())
road = list(map(int, input().split()))
liter = list(map(int, input().split()))

minVal = liter[0]
res = 0
for i in range(n-1):
    if minVal > liter[i]:
        minVal = liter[i]
    res += (minVal * road[i])
    
print(res)