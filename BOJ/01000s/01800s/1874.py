import sys 
input = sys.stdin.readline

# 몇 개의 수
n = int(input())

# 주어지는 리스트
s = []
# 연산자 저장 리스트
op = []
count = 1
temp = True

for i in range(n):
    num = int(input()) # 4 3 6 8 7 5 2 1
    while count <= num:
        s.append(count)
        op.append("+")
        count += 1
    if s[-1] == num:
        s.pop()
        op.append("-")
    else:
        temp = False

if temp == False:
    print("NO")
else:
    for i in op:
        print(i)