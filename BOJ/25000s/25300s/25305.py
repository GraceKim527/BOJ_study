n, k = map(int, input().split()) # 응시자 수, 상을 받는 사람의 수
x = list(map(int, input().split()))

x.sort(reverse=True)
print(x[k-1])