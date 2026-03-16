#2178 미로탐색

from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input().strip())) for _ in range(N)]

dq =deque()
visited = [[0]*M for _ in range(N)]

dq.append((0,0,1))
visited[0][0] = 1

dr = [-1,1,0,0]
dc = [0,0,-1,1]

cnt=0
while dq:
  r,c, dist = dq.popleft()
  if r == N-1 and c == M-1 :
    print(dist)
    break

  for d in range(4):
    nr = dr[d] +r
    nc= dc[d] +c

    if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and board[nr][nc]==1:
      visited[nr][nc] = 1
      dq.append((nr, nc, dist+1))