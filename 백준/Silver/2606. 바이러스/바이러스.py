#2606 바이러스

N = int(input()) # 컴터수
M = int(input()) # 간선

virus = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
  a,b = map(int, input().split())
  virus[a].append(b)
  virus[b].append(a)

def dfs(node):
  visited[node] = 1
  for next in virus[node]:
    if(visited[next] == 0):
      dfs(next)
dfs(1)


print(sum(visited)-1)

