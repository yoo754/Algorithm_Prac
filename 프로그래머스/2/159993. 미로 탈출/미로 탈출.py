from collections import deque

def solution(maps):
    
    answer = 0
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    dq = deque()
    board = []
    
    for i in range(len(maps)):
        board.append(list(maps[i].strip()))
                 
    
    
    def bfs(r, c, target, board):
        dq = deque()
        dq.append((r,c,0))
        
        visited = [[0]*len(board[0]) for _ in range(len(board))]
                
        while dq:
            r,c,dist = dq.popleft()

            if board[r][c] == target :
                return r,c,dist
                break

            for d in range(4):
                nr = dr[d] + r
                nc = dc[d] + c

                if 0<=nr<len(board) and 0<=nc<len(board[0]) and visited[nr][nc] == 0 and board[nr][nc] != 'X':
                    dq.append((nr,nc,dist+1))
                    visited[nr][nc] = 1
        else : return r,c,-1
    
    tamp = [] # 거리 박을 정답 배열
    for j in range(len(board)):
        for k in range(len(board[0])):
            if board[j][k] == 'S':# 시작지점
                r_1, c_1, dist_1 = bfs(j,k,'L',board)
    
    r_2, c_2, dist_2 = bfs(r_1,c_1,'E',board)
    
    if dist_1 != -1 and dist_2 != -1:
        answer = dist_1 + dist_2
    else :
        answer = -1
                
    return answer
