T = int(input())

for i in range(T):
    s = 0
    OX = list(input().split('X'))
    for j in OX:
        cnt = j.count('O')
        if cnt > 0:
            s += sum(range(1, cnt + 1))
    print(s)