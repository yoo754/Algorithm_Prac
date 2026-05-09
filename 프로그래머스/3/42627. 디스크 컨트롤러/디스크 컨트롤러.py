import heapq

def solution(jobs):
    answer = 0
    
    jobs.sort()
    
    pq = []
    cur_time = 0
    idx = 0
    
    while pq or idx < len(jobs):
        while idx < len(jobs) and cur_time >= jobs[idx][0]:
            heapq.heappush(pq, (jobs[idx][1], jobs[idx][0])) 
            idx += 1
            
        if pq:
            ms, plz = heapq.heappop(pq) # 소요시간, 요청시각 (소요시간 젤 짧은것부터 pop)
            cur_time += ms
            answer += (cur_time - plz) # 대기시간
        
        else:
            cur_time = jobs[idx][0]
        
    
    return answer // len(jobs)