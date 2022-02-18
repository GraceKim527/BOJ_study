a,b = input().split()
a = int(a[::-1]) #역순
b = int(b[::-1]) #역순

if a > b:
    print(a)
else:
    print(b)