from collections import deque

def solution(maps):
    answer = 0
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    N = len(maps)
    M = len(maps[0])
    
    visited = [[0]*M for _ in range(N)]
    
    dq = deque()
    dq.append((0,0,1))   
    visited[0][0] = 1
    
    while dq:
        r, c, cnt = dq.popleft()
        
        if r==N-1 and c==M-1 :
            return cnt
            break
        
        for d in range(4):
            nr = dr[d] + r
            nc = dc[d] + c
            
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and maps[nr][nc] == 1 :
                dq.append((nr,nc,cnt+1))
                visited[nr][nc] = 1
                
    else: return -1       
    return cnt