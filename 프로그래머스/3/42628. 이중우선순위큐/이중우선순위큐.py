import heapq

def solution(operations):
    
    min_hq = []
    max_hq = []

    for order in operations:
        eng, nums = map(str, order.split())
        nums = int(nums)
        
        if eng == 'I':
            heapq.heappush(min_hq, (nums))
            heapq.heappush(max_hq, (-nums))

        elif eng == 'D' and min_hq:
            if nums == 1: # 최댓값 삭제
                max_val = -(heapq.heappop(max_hq))
                min_hq.remove(max_val)
                
            else: # 최솟값 삭제
                min_val = heapq.heappop(min_hq)
                max_hq.remove(-min_val)
                
    if min_hq :
        return [-heapq.heappop(max_hq), heapq.heappop(min_hq)]
    else :
        return [0,0]
    
