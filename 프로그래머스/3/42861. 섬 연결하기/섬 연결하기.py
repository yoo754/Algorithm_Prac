import heapq
def solution(n, costs):

    
    def find(x): 
        if parent[x] != x:
            parent[x] = find(parent[x])  # 경로 압축
        return parent[x]
    
    def union (cost, x, y):
        root_x = find(x)
        root_y = find(y)
        
        if root_x != root_y :
            parent[root_y] = root_x
            return True
        
        return False

    hq = []
    dum = 0 # cost 값 저장
    parent = [i for i in range(n)]  
    
    for x, y, z in costs: 
        heapq.heappush(hq, (z, x, y))
    # print(hq)       
    while hq:
        cost, node1, node2 = heapq.heappop(hq)
        
        if union(cost, node1, node2) : #True 반환시
            dum += cost
        else :
            continue
        
        
    return dum