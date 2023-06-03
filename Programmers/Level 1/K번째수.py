## 내 풀이

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        tmp_arr = array[commands[i][0]-1:commands[i][1]]
        tmp_arr.sort()
        answer.append(tmp_arr[commands[i][2]-1])
    return answer

## 다른 사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

## 다른 사람 풀이 2
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
# i,j,k를 저렇게 한 꺼번에 저장할 수 있다는 사실을 잊고 있었다. 