t = int(input())
for _ in range(t):
    test = int(input())
    max = 0
    max_name = ""
    for i in range(test):
        name, alco = input().split()
        alco = int(alco)
        if (alco > max):
            max = alco
            max_name = name
    print(max_name)