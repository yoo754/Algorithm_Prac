# 14502 연구소

from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N,M = map(int, input().split())

# 0빈칸 1벽 2바이러스
arr = [list(map(int, input().split())) for _ in range(N)] # 원본 arr은 보존해야됨

empty_org = []
queue_org = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            queue_org.append((i,j))
        elif arr[i][j] == 0:
            empty_org.append((i,j))

comb = list(combinations(empty_org, 3))
max_safe = []

for tried in comb:
    
    arr_copy = copy.deepcopy(arr)
    queue = copy.deepcopy(queue_org)
    visited = set()
    
    for a,b in tried:
        arr_copy[a][b] = 1
    
    while queue:
        r,c = queue.popleft()
        
        for d in range(4):
            nr, nc = dr[d] + r , dc[d] + c
            
            if 0 <= nr < N and 0 <= nc < M and (nr,nc) not in visited and arr_copy[nr][nc] == 0 :
                arr_copy[nr][nc] = 2
                visited.add((nr,nc))
                queue.append((nr,nc))
    
    cnt = sum(row.count(0) for row in arr_copy)
    max_safe.append(cnt)
    
print(max(max_safe))
            
            
        
        
    
        