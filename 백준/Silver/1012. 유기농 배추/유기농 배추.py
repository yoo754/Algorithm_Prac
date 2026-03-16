#1012 유기농배추

from collections import deque

T = int(input())
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for _ in range(T):
  cnt = 0
  M, N, K = map(int, input().split())
  
  dq = deque()
  visited = set()
  board = [[0]*N for _ in range(M)]

  for _ in range(K):
    X, y = map(int, input().split())
    board[X][y] = 1

  for i in range(M):
    for j in range(N):
      if board[i][j] == 1 :
        dq.append((i,j))
        board[i][j] = 0
        cnt += 1

        while dq :
          r,c = dq.popleft()

          for d in range(4):
            nr = dr[d] + r
            nc = dc[d] + c

            if(0<=nr<M and 0<=nc<N and board[nr][nc] == 1):
              board[nr][nc] = 0
              dq.append((nr,nc))

  
  print(cnt)
