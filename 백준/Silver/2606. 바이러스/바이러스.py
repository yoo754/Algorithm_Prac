from collections import deque

N = int(input()) # 컴퓨터의 수
T = int(input()) # 컴퓨터 쌍의 수

adj = [[] for _ in range(N+1)] 

for _ in range(T): 
  x, y = map(int, input().split()) # 인접 리스트 입력
  adj[x].append(y) # 양방향을 위해 둘 다 저장
  adj[y].append(x)

stack = deque([1]) # 1에서 시작하기 때문에 1을 넣고 시작
visited = set([1]) # 방문지 저장 , 1에서 시작

while stack: # stack이 빌때까지 반복
  now = stack.pop() # 스택에 들어있는 가장 오른쪽 값을 빼냄

  for destination in adj[now]:
    if destination not in visited: # 방문지에 도착지가 없다면
      stack.append(destination) # stack에 도착지를 넣음
      visited.add(destination) # 방문지에도 저장

print(len(visited)-1) # 1번 컴퓨터 제외

