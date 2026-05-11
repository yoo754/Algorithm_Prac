import heapq

def solution(n, s, a, b, fares):
    # 지점의 개수 n, 
    # 출발지점을 나타내는 s, 
    # A의 도착지점을 나타내는 a, 
    # B의 도착지점을 나타내는 b, 
    # 지점 사이의 예상 택시요금을 나타내는 fares가 매개변수
    
    answer = float('inf')
    
    board = [[] for _ in range(n+1)]
    
    for x,y,z in fares: # c가 요금
        board[x].append((z,y))
        board[y].append((z,x))
    
    
    def dij(s, board, n):
        
        dist = [float('inf')] * (n+1)
        dist[s] = 0
        
        hq = []
        heapq.heappush(hq, (0,s)) # 거리값, 시작노드
        
        while hq:
            cost, node = heapq.heappop(hq)

            if cost > dist[node]: # 이미 박혀있는 값이 더 작으면 continue
                continue

            for (weight, new_node) in board[node]:
                new_weight = weight + cost
                if new_weight < dist[new_node] : # new_weight가 더 작으면 업데이트
                    dist[new_node] = new_weight
                    heapq.heappush(hq, (new_weight,new_node))
                
        return dist
            
    new_s = dij(s, board, n)
    new_a = dij(a, board, n)
    new_b = dij(b, board, n)
    
    for i in range(1, n+1):
        answer = min(answer, new_s[i]+new_a[i]+new_b[i] )
    
    return answer

