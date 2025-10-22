from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

N, M = map(int, input().split())

maze = set()
visited = set()

# 걍 1위치를 전부 좌표화
for i in range(N):
    k = input()
    k = list(str(k)) # 공백없는 문자열 리스트화
    m = 0
    for j in k:
        if j == "1":
            maze.add((i,m))
        m += 1

queue = deque([(0,0,0)])

while queue:
    r,c, dist = queue.popleft()
    
    if r == (N-1) and c == (M-1):
        print(dist+1)
        break
        
    for d in range(4):
        nr, nc = dr[d] + r, dc[d] + c
                 
        if  0 <= nr < N and 0 <= nc < M and (nr, nc) in maze and (nr, nc) not in visited:
                            
            visited.add((nr, nc))
            queue.append((nr, nc, dist+1))
            