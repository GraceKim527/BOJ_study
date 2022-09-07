n = int(input()) 

cute = 0
nocute = 0
for i in range(n):
    result = int(input())
    if result == 1:
        cute += 1
    else:
        nocute += 1

if cute > nocute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")