from collections import deque
import copy
def solution(tickets):
    answer = []
    # 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
    
    tickets.sort()
    
    # 현재위치, 경로, visited
    dq = deque()
    dq.append(("ICN", ["ICN"], [0] * len(tickets)))
    
    print(dq)
    
    while dq:
        now, route, visited = dq.popleft()
        
        if len(route) == len(tickets) + 1:
            return route
        
        for i in range(len(tickets)) :
            candi = tickets[i][1]
            
            if tickets[i][0] == now and visited[i] == 0:
                new_visited = copy.deepcopy(visited)
                new_visited[i] = 1
                dq.append((tickets[i][1], route + [tickets[i][1]], new_visited))


    return answer