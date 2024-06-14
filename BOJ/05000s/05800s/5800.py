import sys 
input = sys.stdin.readline

k = int(input()) # 고등학교 반의 수

for i in range(k):
  grades = []
  minimum = 0
  grades = list(map(int, input().split()))
  num = grades[0]
  grades.remove(num)
  grades.sort(reverse=True)
  for j in range(len(grades) - 1):
    minimum = max(grades[j] - grades[j+1], minimum)
    # print(minimum)
  print(f"Class {i+1}")
  print(f"Max {max(grades)}, Min {min(grades)}, Largest gap {minimum}")