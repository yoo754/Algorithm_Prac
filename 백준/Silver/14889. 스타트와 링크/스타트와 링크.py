from itertools import combinations, permutations

n = int(input())

arr = []

for i in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums)
    
num = []

for i in range(n):  
    num.append(i)

n2 = int(n/2)
nCr = list(combinations(num,n2))

result = []
for i in range(int(len(nCr)/2)):
    num1 = [x for x in num if x not in nCr[i]] 
    
    nCrS = list(combinations(nCr[i],2)) # nCr 2개로 분리한 값
    nCrR = list(combinations(num1,2)) # nCr에 해당하지 않는 값들 조합

    Ssum = 0
    Rsum = 0
    
    for j in range(len(nCrS)):

        Ssum += arr[nCrS[j][0]][nCrS[j][1]]
        Ssum += arr[nCrS[j][1]][nCrS[j][0]]
        
        Rsum += arr[nCrR[j][0]][nCrR[j][1]]
        Rsum += arr[nCrR[j][1]][nCrR[j][0]]
    
    result.append(abs(Ssum-Rsum))
    
print(min(result))