n, m = map(int, input().split()) # 기타줄 개수, 브랜드 개수

minPack, minSingle = 1001, 1001
for i in range(m):
    p, s = map(int, input().split())
    minPack = min(minPack, p)
    minSingle = min(minSingle, s)

result = 0

# 패키지를 테스트
if minPack > minSingle * 6:
    result += n * minSingle
else:
    result += (n//6) * minPack
    # 남은 갯수를 패키지, 낱개로 처리하는 방법
    if (n % 6) * minSingle > minPack:
        result += minPack
    else:
        result += (n % 6) * minSingle

print(result)