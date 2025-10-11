from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
    
not_visited = set(range(1, N+1))
line = 0

while not_visited:
    line += 1
    stack = deque([not_visited.pop()])
    
    while stack:
        now = stack.pop()
        for desti in arr[now]:
            if desti in not_visited:
                not_visited.remove(desti)
                stack.append(desti)


print(line)