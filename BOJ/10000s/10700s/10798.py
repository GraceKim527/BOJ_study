test_list = [[10]*15 for i in range(5)]
 
for i in range(5):
    a = list(input())
    a_len = len(a)
    for j in range(a_len):
        test_list[i][j] = a[j]
 
for i in range(15):
    for j in range(5):
        if test_list[j][i] == 10:
            continue
        else:
            print(test_list[j][i],end='')