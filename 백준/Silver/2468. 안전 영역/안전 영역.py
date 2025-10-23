# 2468 안전 영역

from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

N = int(input())
arr = []
for i in range(N):
    dum = list(map(int, input().split()))
    arr.append(dum)
 
cnt_list = []

min_h = min(map(min, arr))
max_h = max(map(max, arr))

for k in range(min_h - 1, max_h + 1):
    cnt = 0
    flood = set()
    stack = deque()
    visited = set()

    for j in range(N):
        for l in range(N):
           if arr[j][l] > k :
               flood.add((j,l))
               stack.append((j,l))
                   
    while stack:
        r,c = stack.pop()
        
        if (r,c) not in visited :
            visited.add((r,c))
            
            queue = deque([(r,c)])
            
            while queue:
                r,c = queue.popleft()
                
                for d in range(4):
                    nr, nc = dr[d] + r, dc[d] + c
                    
                    if (nr,nc) not in visited and (nr, nc) in flood:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        
            cnt += 1
    cnt_list.append(cnt) 
print(max(cnt_list))    
                    
                