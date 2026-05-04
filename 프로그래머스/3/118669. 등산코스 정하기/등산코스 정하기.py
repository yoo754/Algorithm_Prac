import heapq

def solution(n, paths, gates, summits):
    summit_set = set(summits)
    
    board = [[] for _ in range(n+1)]
    
    for a,b,c in paths:
        board[a].append((b,c))
        board[b].append((a,c))
        
    dist = [float('inf')] * (n+1)
    
    dq = []
    
    for i in gates:
        dist[i] = 0
        heapq.heappush(dq, (0, i)) #cost, node
    
    while dq:
        cost , node = heapq.heappop(dq)

        if cost > dist[node]:
            continue
            
        if node in summit_set: 
            continue

        for next_code, weight in board[node]:
            new_cost = max(cost, weight)
            if new_cost < dist[next_code] : # intensity의 최솟값 찾아야함
                dist[next_code] = new_cost
                heapq.heappush(dq, (new_cost, next_code))
            

    intensity = float('inf')
    answer = 0
    
    for j in sorted(summits):
        if dist[j] < intensity :
            intensity = dist[j]
            answer = j
    
    return [answer, intensity]

