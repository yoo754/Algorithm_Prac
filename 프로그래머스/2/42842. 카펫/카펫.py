def solution(brown, yellow):
    
    total = brown + yellow
    
    for i in range(3, total // 3 + 1) : # 중간이 있으려면 3줄부터됨
        if total % i == 0 :
            j = total // i
            if 2*i + 2*j - 4 == brown :
                return [j, i]
