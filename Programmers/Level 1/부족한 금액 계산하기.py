def solution(price, money, count):
    list = []
    for i in range(1, count+1):
        list.append(i*price)
    
    if sum(list) > money:
        return sum(list) - money
    else:
        return 0