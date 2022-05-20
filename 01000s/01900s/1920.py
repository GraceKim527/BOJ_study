############## 시간 초과 ################
# n = int(input()) # n개의 정수
# n_lst = list(map(int, input().split()))
    
# m = int(input()) # m개의 정수
# m_lst = list(map(int, input().split()))
    
# for i in range(len(n_lst)):
#     if m_lst[i] in n_lst:
#         print(1)
#     else:
#         print(0)

def binary(elem, n_lst, start=0, end=None):
    if end == None:
        end = len(n_lst) -1
    if start > end:
        return 0
    
    mid = (start + end) // 2
    
    if elem == n_lst[mid]:
        return 1
    elif elem < n_lst[mid]:
        end = mid - 1
    elif elem > n_lst[mid]:
        start = mid + 1
    return binary(elem, n_lst, start, end)

n = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()

m = int(input())
m_lst = list(map(int, input().split()))

for i in range(len(m_lst)):
    print(binary(m_lst[i], n_lst))