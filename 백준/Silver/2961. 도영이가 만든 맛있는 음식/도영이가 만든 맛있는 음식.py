from itertools import combinations

n = int(input()) 

nums = []

for i in range(n):
    nums1, nums2 = map(int, input().split())
    nums.append((nums1, nums2))

result = []
for i in range(1, n+1):
    for j in combinations(nums, i):
        xs = [x for x,_ in j]
        ys = [y for _, y in j]
        
        x = 1
        
        for k in range(len(xs)):
            x *= xs[k]        

        result.append(abs(x -sum(ys)))
        
        
print(min(result))