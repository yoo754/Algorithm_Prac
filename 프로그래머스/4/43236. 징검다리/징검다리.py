def solution(distance, rocks, n):
    answer = 0
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    
    left = 0
    right = distance
    
    while left <= right :
        mid = (left+right) // 2
        
        remove = 0
        prev = 0
        
        for i in range(1, len(rocks)):
            if rocks[i] - rocks[prev] < mid:
                remove += 1
                
            else :
                prev = i
                
        if remove <= n:
            answer = mid
            left = mid + 1
             
        else:
            right = mid - 1

        
    return answer