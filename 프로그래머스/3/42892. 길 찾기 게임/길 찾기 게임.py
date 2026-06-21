import copy
import sys
sys.setrecursionlimit(300000)

def solution(nodeinfo):
    answer_pre = []
    answer_pos = []
    
    tree = [None] * (len(nodeinfo) + 1)  # tree[node번호] = (left, right)
    
    # 함수를 총 3개 만들어야됨
    # y가 같을 때 x가 큰게 오른쪽 노드
    # 1. node 생성
    def insert(root, node): # 들어오면 각 노드들은 [x,y,idx] 뱉어냄
        if tree[root[2]] is None:
            tree[root[2]] = [None, None]
        # 새 노드를 left에 넣을지 right에 넣을지 → x 비교
        if root[0] < node[0] :
            # 그 자리가 비어있는지 아닌지 → tree[root[2]] 가 None인지
            if tree[root[2]][1] == None:
                tree[root[2]][1] = node[2]
            else : # 자리에 노드있을 때
                insert(nodes[tree[root[2]][1]-1], node)
                
        else :
            if tree[root[2]][0] == None:
                tree[root[2]][0] = node[2]
            else : # 자리에 노드있을 때
                insert(nodes[tree[root[2]][0]-1], node)
    
    # tree = [None, [None, 8], [None, 3], None, [6, 1], None, [None, 9], [4, 2], [5, None], None]
    
    # 2. 전위순회
    def pre(node):
        if node is None :
            return
        
        answer_pre.append(node)
        if tree[node] is None:
            return
        pre(tree[node][0])
        pre(tree[node][1])
        
    # 3. 후위순회
    def pos(node):
        if node is None :
            return
        if tree[node] is None:
            answer_pos.append(node)
            return
        pos(tree[node][0])
        
        pos(tree[node][1])
        
        answer_pos.append(node)
        
    
    # 소팅을 하기전에 미리 쟤네한테 idx 알려줘야하는데
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodes = copy.deepcopy(nodeinfo)
    # 부모노드부터 소팅하고
    nodeinfo = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    # 소팅 결과 
    # [[8, 6, 7], [3, 5, 4], [11, 5, 2], [1, 3, 6], [5, 3, 1], [13, 3, 3], [2, 2, 9], [7, 2, 8], [6, 1, 5]]
    
    # 노드만들기
    root = nodeinfo[0]
    for node in nodeinfo[1:]:
        insert(root, node)
    
    # 전위순회
    pre(root[2])
    # 후위순회
    pos(root[2])

    return [answer_pre,answer_pos]