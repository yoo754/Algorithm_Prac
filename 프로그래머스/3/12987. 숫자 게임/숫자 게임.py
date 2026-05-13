from collections import deque
def solution(A, B):

    A.sort()
    B.sort()
    
    dq = deque(A)
    
    cnt = 0
    
    for b in B:
        if dq and b > dq[0]: # b가 A 가장 작은 값보다 크면
            dq.popleft()
            cnt += 1

    return cnt