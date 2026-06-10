def solution(info, edges):
    answer = 0
    # info 0은 양, 1은 늑대
    # edges [부모 노드 번호, 자식 노드 번호]
    
    tree = [[] for _ in range(len(info))]
    
    for x,y in edges :
        tree[x].append(y)
    
    def dfs(node, candi, sheep, wolf) :
        nonlocal answer
        
        if info[node] == 0:
            sheep += 1
        else :
            wolf += 1
        
        if wolf >= sheep :
            return
        
        candi += tree[node]
        answer = max(answer, sheep)
        
        for next_node in candi:
            new_candi = candi[:]
            new_candi.remove(next_node)
            dfs(next_node, new_candi, sheep, wolf)

    candi = []

    dfs(0, candi, 0, 0)
    
    return answer
