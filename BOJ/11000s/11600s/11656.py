import sys
input = sys.stdin.readline

s = input()
s_list = []

for i in range(len(s)-1):
    s_list.append(s[i:])
    s_list[i] = s_list[i].replace("\n", "")

s_list.sort()
for i in range(len(s_list)):
    print(s_list[i])