from itertools import permutations

def solution(numbers):
    answer = 0
    
    ans = set()

    dum = [[] for _ in range(len(numbers))] 
    
    for i in range(len(numbers)):
        dum[i] = numbers[i]
        
    # 조합될 수 있는 모든 수 set에 넣고
    for i in range(1, len(dum) + 1):
        for p in permutations(dum, i):
            ans.add(int(''.join(p)))
    
    print(ans)
    
    cnt = 0
    for i in ans:
        if i < 2:  # 0, 1 제외
            continue
            
        is_prime = True
        
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break  
                
        if is_prime:
            cnt += 1
 
    return cnt
