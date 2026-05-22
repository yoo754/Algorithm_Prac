def solution(numbers, target):
    
    def dfs(idx, sums):
        
        if idx == len(numbers):
            if target == sums:
                return 1
            else :
                return 0

        return dfs(idx+1, sums + numbers[idx]) + dfs(idx+1, sums - numbers[idx])

    return dfs(0,0)  

