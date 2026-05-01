from collections import deque
def solution(n, wires):
    dum = [] # answer 저장할 리스트
    
    
    def bfs(start, board):
        visited = [0]*(n+1)
        dq = deque()
        dq.append((start))
        visited[start] = 1
        cnt = 1
        
        while dq:
            now = dq.popleft()
            
            for nxt in board[now]:
                if visited[nxt] == 0:
                    dq.append((nxt))
                    visited[nxt] = 1
                    cnt += 1 
                    
        return cnt
            
            
    for i in range(len(wires)):      
        board = [[] for _ in range(n+1)]
        for j in range(len(wires)):
            if j == i: continue       
            a, b = wires[j]           
            board[a].append(b)
            board[b].append(a)

        # 이쪽 값
        dum1 = bfs(a, board)
        # 반대 값
        dum2 = n - dum1
        # 저장할 값
        dum.append(abs(dum1-dum2))
    
    return min(dum)