from itertools import combinations

lst = []

for i in range(9):
    a = int(input())
    lst.append(a)

nums = sum(lst)-100

for i in combinations(lst, 2):
    if sum(i) == nums:
        lst.remove(i[0])
        lst.remove(i[1])

        
for i in range(len(lst)):
    print(lst[i])
    