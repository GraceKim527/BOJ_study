import sys 
input = sys.stdin.readline

vowel = ['a', 'e', 'i', 'o', 'u']
accept = ['ee', 'oo']

while True:
  x = 0
  y = 0
  testcase = input().rstrip()
  if testcase == 'end':
    break
  
  # 카운트
  cnt = 0
  for i in vowel:
    if i in testcase:
      cnt += 1
  
  # 모음이 없으면 안됨    
  if cnt < 1:
    print(f'<{testcase}> is not acceptable.')
    continue
  
  # 모음이 3개 연속, 자음이 3개인 경우
  for i in range(len(testcase) - 2):
    if testcase[i] in vowel and testcase[i+1] in vowel and testcase[i+2] in vowel:
      x = 1
    elif not(testcase[i] in vowel) and not(testcase[i+1] in vowel) and not(testcase[i+2] in vowel):
      x = 1
      
  if x == 1:
    print(f'<{testcase}> is not acceptable.')
    continue
  
  # 같은 글이 연속 두 개인지 체크, 'e'나 'o'는 예외
  for i in range(len(testcase) - 1):
    if testcase[i] == testcase[i+1]:
      if testcase[i] == 'e' or testcase[i] == 'o':
        continue
      else:
        y = 1
        
  if y == 1:
    print(f'<{testcase}> is not acceptable.')
    continue
  
  print(f'<{testcase}> is acceptable.')