# 15651 N과 M(3)

from itertools import product 

N, M = map(int, input().split())

nums = []

for i in range(1,N+1):
    nums.append(i)    
        

for j in product(nums, repeat=M):
    print(*j)