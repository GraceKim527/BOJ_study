import sys
input = sys.stdin.readline

def binary_search(target, array, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target: 
        return binary_search(target, array, start, mid-1)
    else:
        return binary_search(target, array, mid+1, end)

for _ in range(int(input())):
    N = int(input())
    note_1 = list(map(int, input().split()))
    M = int(input())
    note_2 = list(map(int, input().split()))
    
    note_1.sort()
    for note in note_2: # 1
        result = binary_search(note, note_1, 0, N - 1) 
        if result == None:
            print(0)
        else:
            print(1)