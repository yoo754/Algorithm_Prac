# 3055 탈출

from collections import deque

# 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다. 
# 비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

N, M = map(int, input().split())

dr = [-1,1,0,0]
dc = [0,0,-1,1]

board = [list(map(str, input().strip())) for _ in range(N)]

dq = deque()
water = deque()
visited = [[0]*M for _ in range(N)]

bb_r = 0
bb_c = 0

for i in range(N) :
    for j in range(M) :
        if board[i][j] == 'S': 
            dq.append((i, j, 0))
        if board[i][j] == 'D':
            bb_r = i
            bb_c = j
        if board[i][j] == '*' :
            water.append((i,j))
 
# print(dq)
# print(water)   

         
while dq:
    
    size = len(water)
    
    for _ in range(size):
        wr, wc = water.popleft()
        
        for d in range(4):
            nwr = dr[d] + wr
            nwc = dc[d] + wc
            
            if 0<=nwr<N and 0<=nwc<M and board[nwr][nwc] == '.':
                board[nwr][nwc] = '*'
                water.append((nwr, nwc))
    
    for _ in range(len(dq)) :
        
        r, c, day = dq.popleft()
        
        if r == bb_r and c == bb_c :
            print(day)
            exit()
        
        for d in range(4):
            nr = dr[d] + r
            nc = dc[d] + c
            
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and (board[nr][nc] == '.' or board[nr][nc] == 'D') :
                visited[nr][nc] = 1
                dq.append((nr, nc, day+1))

else:
    print("KAKTUS")               