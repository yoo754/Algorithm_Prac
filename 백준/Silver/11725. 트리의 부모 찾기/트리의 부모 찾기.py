# 11725 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

N = int(input())

parent = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
  m, s = map(int, input().split())
  parent[m].append(s)
  parent[s].append(m)

def dfs(node) :
  for next in parent[node]:
    if(visited[next] == 0) :
      visited[next] = node
      dfs(next)

dfs(1)

for i in range(2, N+1):
  print(visited[i])