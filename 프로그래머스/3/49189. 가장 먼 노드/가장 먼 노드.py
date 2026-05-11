# from collections import deque
import heapq

def solution(n, edge):
    answer = 0
    board = [[] for _ in range(n+1)]
             
    for a,b in edge :
        board[a].append(b)
        board[b].append(a)
        
    
    dist = [float('inf')] * (n+1)
    dist[1] = 0
    dist[0] = -1

    hq = []
    heapq.heappush(hq, (0,1)) # 이동값, 시작노드 

    while hq:
        cost, node = heapq.heappop(hq)
        
        if cost > dist[node]:  
            continue
            
        for new_node in board[node]:
            new_cost = cost+1
            if dist[new_node] > new_cost:
                dist[new_node] = new_cost
                heapq.heappush(hq, (new_cost, new_node))
        
    
#     다익스트라..
#     최소거리... 그럼 얘도 heapq인가 이동거리 기록하고 가장 max값 찾아서 그게 리스트에 몇개 있는지?
#     그럼 가중치, 노드값 끌고 다녀야됨
#     1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 
    
    return dist.count(max(dist))