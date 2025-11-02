# 9663 N-Queen

N = int(input())

updown = [False] * N # 상하 확인
right = [False] * (2 * N - 1) # 오른쪽 대각선 확인
left = [False] * (2 * N - 1) # 왼쪽 대각선 확인

cnt = 0

def n_queen(depth): # depth 행
    
    global cnt
    
    if depth == N:
        cnt += 1
        return
    
    for i in range(N):
        if updown[i] == 1 or left[depth-i] == 1 or right[depth+i] == 1:
            continue
        
        updown[i] = True
        left[depth-i] = True
        right[depth+i] = True
        
        n_queen(depth+1)
        
        updown[i] = False
        left[depth-i] = False
        right[depth+i] = False
        

n_queen(0)

print(cnt)
       
    