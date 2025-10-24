# 7576 토마토 (2차원)

from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

M, N = map(int, input().split())

arr = []

for i in range(N):
    dum = list(map(int, input().split()))
    arr.append(dum)

tomato = [[0]*M for _ in range(N)]
visited = set()
queue = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tomato[i][j] = 1
            queue.append((i,j,0))
        elif arr[i][j] == -1:
            tomato[i][j] = -1 # 아예 토마토가 없음
        

while queue:
    r,c, day = queue.popleft()
        
    for d in range(4):
        nr, nc = dr[d] +r , dc[d] +c
                
        if (nr, nc) not in visited and 0 <= nr < N and 0 <= nc < M and tomato[nr][nc] == 0 :
            tomato[nr][nc] = 1
            visited.add((nr, nc))
            queue.append((nr, nc, day+1))

                       
for l in range(N):
    for o in range(M):
        if tomato[l][o] == 0:
            print(-1)
            break  
    else:
        continue
    break  
else:
    print(day)

