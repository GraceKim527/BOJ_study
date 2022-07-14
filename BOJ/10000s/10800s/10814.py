n = int(input())
member_list = []

for _ in range(n):
    age, name = map(str, input().split())
    member_list.append((age, name))

member_list.sort(key = lambda x: int(x[0])) # (age, name)중 age로만 비교

for i in member_list:
    print(i[0], i[1])