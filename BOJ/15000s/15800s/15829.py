import sys 
input = sys.stdin.readline

L = int(input())
M = 1234567891
r = 31

user = input()
answer = 0

for i in range(L):
    num = ord(user[i]) - 96 
    answer += num * (r ** i)

print(answer % M)