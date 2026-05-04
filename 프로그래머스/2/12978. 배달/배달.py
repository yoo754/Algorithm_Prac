import heapq

def solution(N, road, K):
    answer =0
    board = [[] for _ in range(N+1)]
    for a,b,c in road:
        board[a].append((b,c))
        board[b].append((a,c))
    
    dist = [float('inf')] * (N+1)
    dist[1] = 0
    dq = [(0,1)] #cost, node
    
    while dq:
        cost, node = heapq.heappop(dq)
        
        if cost > dist[node]:
            continue
            
        for next_node, weight in board[node]:
            new_cost = cost + weight
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(dq, (new_cost, next_node))
        
    cnt = 0
    for i in dist:
        if i <= K:
            cnt += 1


    return cnt