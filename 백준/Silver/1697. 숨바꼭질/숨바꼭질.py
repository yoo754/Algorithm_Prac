# 1697 숨바꼭질

from collections import deque


N, K = map(int, input().split())

queue = deque([(N,0)]) # 위치, 시간
visited = set([N])

# 걷는다면 1초 후에 X-1 또는 X+1로 이동
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동

while queue:
    p, t = queue.popleft()
    
    if p == K :
        print(t)
        break
           
    for next in (p-1, p+1, p*2):
        if 0 <= next <= 100000 and next not in visited :
            visited.add(next)
            queue.append((next, t+1))
