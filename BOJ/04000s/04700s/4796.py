case = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    rest = (v // p) * l
    rest += min((v % p), l)
    print("Case {}: {}".format(case, rest))
    case += 1