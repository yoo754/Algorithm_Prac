from collections import deque

N, M, V = map(int, input().split()) # 정점, 간선, 시작번호

arr = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
    

stack_dfs = deque([V])
stack_bfs = deque([V])

visited_dfs = []
visited_bfs = []


while stack_dfs :
    now = stack_dfs.pop()
    if now not in visited_dfs:
        visited_dfs.append(now)
        for desti in sorted(arr[now], reverse=True): # 큰번호부터 넣어야 작은번호부터 pop
            if desti not in visited_dfs:
                stack_dfs.append(desti)
                
while stack_bfs :
    now = stack_bfs.popleft()
    if now not in visited_bfs:
        visited_bfs.append(now)
        for desti in sorted(arr[now]):
            if desti not in visited_bfs:
                stack_bfs.append(desti)

            
print(*visited_dfs)
print(*visited_bfs)


    