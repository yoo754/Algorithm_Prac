from collections import deque

def solution(maps):
    answer = []
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    
    board = [[] for _ in range(len(maps))]
    for k in range(len(maps)):
        board[k] = list(map(str, maps[k].strip()))
        
    N = len(board)
    M = len(board[0])
    
    visited = [[0] * M for _ in range(N)]
    dq = deque()
    
    
    for i in range(N):
        for j in range(M):
            if board[i][j] != 'X' and visited[i][j] == 0:
                dq.append((i,j))
                visited[i][j] = 1
                dist = 0
                
                while dq:
                    r,c = dq.popleft()
                    dist += int(board[r][c])
                    # print(dist)
                    
                    for d in range(4):
                        nr = dr[d] + r
                        nc = dc[d] + c
                        
                        if 0 <= nr < N and 0<=nc<M and visited[nr][nc] == 0 and board[nr][nc] != 'X':
                            visited[nr][nc] = 1
                            dq.append((nr, nc))
                            
                answer.append(dist)
        
    answer.sort()
    
    if not answer :
        answer.append(-1)
        return answer
                
    return answer
