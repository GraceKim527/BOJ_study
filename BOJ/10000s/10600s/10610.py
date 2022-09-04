n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print("".join(n))
# .join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c']의 리스트를 'abc' 문자열로 합쳐서 반환해준다.