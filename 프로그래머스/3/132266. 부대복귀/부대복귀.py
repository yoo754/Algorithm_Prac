from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    maps = [[] for _ in range(n+1)]

    for a, b in roads:
        maps[a].append(b)
        maps[b].append(a)
    
    dq = deque()
    dq.append(destination)  
    
    dist = [-1] * (n+1)
    dist[destination] = 0
    
    while dq:
        now = dq.popleft()
        for j in maps[now]:
            if dist[j] == -1:
                dist[j] = dist[now] + 1
                dq.append(j)
    
    for s in sources:        
        answer.append(dist[s])
                    
    return answer