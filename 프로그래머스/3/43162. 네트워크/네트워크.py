from collections import deque
def solution(n, computers):
    answer = 0
    #   1  2  3
    # 1[1, 1, 0], 
    # 2[1, 1, 0], 
    # 3[0, 0, 1]

    cnt = 0
    visited = [0] * n
    
    for i in range(n):
        
        if visited[i] == 1 :
            continue
            
        cnt += 1    
        dq = deque()
        dq.append(i)
        visited[i] = 1
        
        
        while dq:
            node = dq.popleft()

            for j in range(n): 
                if computers[node][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dq.append(j)
                    
    return cnt