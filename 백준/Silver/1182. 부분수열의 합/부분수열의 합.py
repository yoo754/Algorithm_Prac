# 1182 부분수열의 합
from itertools import combinations

N,S = map(int, input().split())

nums = list(map(int, input().split()))

fin = 0

for i in range(1,N+1):
    comb = list(combinations(nums, i))
    for j in range(len(comb)):
        if sum(comb[j]) == S :
            fin += 1
    
print(fin)