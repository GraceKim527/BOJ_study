# 내가 푼 코드

def solution(s):
    if ( len(s) == 4 or len(s) == 6 ) and s.isdigit() == True:
        return True
    else:
        return False
    

# 이상적 코드
def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]
