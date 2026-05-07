from collections import deque

def solution(n, results):

    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    
    
    for a,b in results:
        win[a].append(b)
        lose[b].append(a)
        
    cnt = 0 # return 값 저장할 곳
    
    
    for i in range(1,n+1):
        
        dq = deque()
        dq.append((i)) # start node
        visited = [0]*(n+1)
        visited[i] = 1

        while dq:
            node = dq.popleft()
            
            for a in win[node]:
                if visited[a] == 0 :
                    visited[a] = 1
                    dq.append(a)
        
        dq = deque()           
        dq.append((i))
        
        while dq:
            node = dq.popleft()
            
            for a in lose[node]:
                if visited[a] == 0 :
                    visited[a] = 1
                    dq.append(a)
        
        # visited에서 True 개수 - 1(자기 자신) = n-1이면 순위 확정
        N = 0
        for i in range(len(visited)):
            if visited[i] == 1:
                N += 1
            
        if (N - 1) == (n-1):
            cnt += 1
            
    # print(cnt)
    
    return cnt

    