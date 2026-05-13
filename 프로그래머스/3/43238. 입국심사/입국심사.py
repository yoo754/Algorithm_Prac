def solution(n, times):
    answer = 0
    
    min_time = 1
    max_time = max(times) * n
    
    while min_time <= max_time:
        mid = (max_time + min_time) // 2
        
        # mid분 동안 모든 심사관이 처리할 수 있는 총 인원
        total = sum(mid // i for i in times)
        
        # 검사받을 인원보다 많으면
        if total >= n:
            answer = mid
            # 더 짧은 시간으로 줄여서 탐색
            max_time = mid - 1
            
        else :
            # 더 긴 시간으로 늘려서 탐색
            min_time = mid + 1
            
    return answer