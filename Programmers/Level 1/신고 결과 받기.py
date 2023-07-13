def solution(id_list, report, k):
    report = list(set(report))
    answer = {x: 0 for x in id_list}
    reports = {x: 0 for x in id_list} 
    
    for r in report:
        reports[r.split()[1]] += 1 
        
    for r in report:
        if reports[r.split()[1]] >= k:
            answer[r.split()[0]] += 1
    return list(answer.values())