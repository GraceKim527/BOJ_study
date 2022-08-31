x = int(input()) # 금액
n = int(input()) # 종류 수

result = 0
for i in range(n):
    amount, units = map(int, input().split())
    
    result += amount * units

print("Yes" if result == x else "No")