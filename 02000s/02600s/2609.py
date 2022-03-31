#사실 파이썬 내장함수인 import math를 사용해서 풀어도 된다.
a, b = map(int, input().split())
def gcd(a, b): #Greatest Common Divisor
    while b > 0:
        a, b = b, a % b #b로 나누었을 때 나머지로 다시 나누어서 계산.
    return a

def lcm(a, b): #Least Common Multiple
    return a * b // gcd(a,b) #최대공약수로 나누어주면 최소공배수.

print(gcd(a,b))
print(lcm(a,b))