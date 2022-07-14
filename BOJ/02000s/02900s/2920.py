scale = list(map(int, input().split())) # 음계

if scale == sorted(scale): #sorted : 순서대로 정렬, 정렬된 리스트 반환
    print("ascending")
elif scale == sorted(scale, reverse=True):
    print("descending")
else:
    print("mixed")