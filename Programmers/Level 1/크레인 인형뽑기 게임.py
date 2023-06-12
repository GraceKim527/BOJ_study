## 내 풀이

def solution(board, moves):
    bucket = []
    answer = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                # 바구니 내에서 수가 같다면
                if bucket[-1:] == bucket[-2:-1]:
                    answer += bucket[-1:]
                    bucket = bucket[:-2]
                break
    return len(answer)*2