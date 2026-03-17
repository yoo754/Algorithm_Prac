#10026 적록색약
from collections import deque

N = int(input())
board = [list(map(str, input().strip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
answer = []
dr = [-1,1,0,0]
dc = [0, 0, -1,1]
cnt = 0

def bfs(i, j):
  dq = deque()
  dq.append((i,j))
  visited[i][j] = 1
  color = board[i][j]

  while dq:
        r,c = dq.popleft()

        for d in range(4):
          nr = dr[d] + r
          nc = dc[d] + c

          if 0<=nr<N and 0<=nc<N and board[nr][nc] == color and visited[nr][nc] == 0 :
            visited[nr][nc] = 1
            dq.append((nr,nc))

# 일반인
for i in range(N):
  for j in range(N):
    if visited[i][j] == 0:
      bfs(i, j)
      cnt += 1
answer.append(cnt)
cnt = 0
visited = [[0]*N for _ in range(N)]

# 적록색약
for i in range(N):
  for j in range(N):
    if board[i][j] == 'G':
      board[i][j] = 'R'
for i in range(N):
  for j in range(N):
    if visited[i][j] == 0:
      bfs(i, j)
      cnt += 1
answer.append(cnt)    
      


print(*answer)
