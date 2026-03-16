#4963 섬의 개수

from collections import deque

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

while True:

  W, H = map(int, input().split())
  cnt = 0

  if W==0 and H==0:
    break

  board = [list(map(int, input().split())) for _ in range(H)]
  dq = deque()

  for i in range(H):
    for j in range(W):
      if board[i][j] == 1 :
        dq.append((i,j))
        board[i][j] = 0
        cnt += 1

        while dq:
          r,c = dq.popleft()

          for d in range(8):
            nr = dr[d] + r
            nc = dc[d] + c 

            if 0<=nr<H and 0<=nc<W and board[nr][nc] == 1:
              board[nr][nc] = 0
              dq.append((nr,nc))

  print(cnt)
