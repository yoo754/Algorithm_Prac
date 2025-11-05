# 15686 치킨 배달

# 0은 빈 칸, 1은 집, 2는 치킨집

from itertools import combinations

N , M = map(int, input().split()) # N*N 도시사이즈, M 치킨집 개수

house = []
bbq = []
arr = []

for _ in range(N): 
    dum = list(map(int, input().split()))
    arr.append(dum)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i,j))
        elif arr[i][j] == 2:
            bbq.append((i,j))

# 조합만들기
comb = list(combinations(bbq, M))

# 가장 가까운 치킨집 구하기
def decision(x,y,comb):
    for i in range(len(comb)):
        dummy = []
        for a,b in comb:
            now = abs(a-x) + abs(b-y)
            dummy.append((now,a,b))
    
        return min(dummy)[0]
            
fin = []

for i in comb:
    sum = 0
    for x,y in house:
        sum += decision(x,y,i)
    fin.append(sum)
    
print(min(fin))