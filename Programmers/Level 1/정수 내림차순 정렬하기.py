def solution(n):
    n_list = list(str(int(n)))
    n_list.sort(reverse = True)
    return int("".join(n_list))