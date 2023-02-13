n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력받기
for _ in range(n):
    students.append(input().split())

# 튜플이 여러 개의 원소로 구성되면, 첫 번째 원소의 순서에 맞게 정렬되고, 만약 첫 번째가 같다면 두 번째 원소의 순서에 맞게 정렬되는 특성이 있다.
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])