## 시간초과 코드

def solution(players, callings):
    for call in callings:
        idx = players.index(call)
        temp = players[idx-1]
        players[idx-1] = players[idx]
        players[idx] = temp
    return players

## 제대로 된 풀이

def solution(players, callings):
    player_dict = {p:i for i, p in enumerate(players)} # 선수 : 등수
    idx_dict = {i:p for i,p in enumerate(players)} # 등수 : 선수
    
    for call in callings:
        loc = player_dict[call] # 현재 등수의 인덱스
        loc2 = loc - 1 # 앞 등수의 인덱스
        call2 = idx_dict[loc2] # 앞 선수
        
        idx_dict[loc2] = call
        idx_dict[loc] = call2
        
        player_dict[call] = loc2
        player_dict[call2] = loc
    return list(idx_dict.values())