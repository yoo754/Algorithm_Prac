# 7569 토마토

from collections import deque

M, N, H = map(int, input().split())

board = []

for _ in range(H):
  layer = [list(map(int, input().split())) for _ in range(N)]
  board.append(layer)


dr = [-1,1,0,0,0,0]
dc = [0,0,-1,1,0,0]
dh = [0,0,0,0,-1,1]

dq = deque()

for i in range(H):
  for j in range(N):
    for k in range(M):
      if board[i][j][k] == 1:
        dq.append((i,j,k))


while dq:
  h, r, c = dq.popleft()

  for d in range(6):
    nh = dh[d] + h
    nr = dr[d] + r
    nc = dc[d] + c

    if 0<=nh<H and 0<=nr<N and 0<=nc<M and board[nh][nr][nc] == 0:
      board[nh][nr][nc] = board[h][r][c] + 1
      dq.append((nh,nr,nc))

result = 0
possible = True

for i in range(H):
  for j in range(N):
    for k in range(M):
      if board[i][j][k] == 0:
        possible = False
        break 
      result = max(result, board[i][j][k])

if not possible:
    print(-1)
else:
    print(result - 1)