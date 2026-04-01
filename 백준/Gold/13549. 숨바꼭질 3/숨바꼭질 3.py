#13549 숨바꼭질 3

from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int, input().split())


dq = deque()
dq.append((N,0))

visited = [False] * 100001

while True:
  now, time = dq.popleft()

  if visited[now]:
    continue
  visited[now] = True

  if now == K :
    print(time)
    break

  for np in [now * 2, now+1, now-1]:
    if 0<= np <= 100000 and not visited[np] : 
      if np == now * 2:
        dq.appendleft((np,time))
      else :
        dq.append((np,time+1))
