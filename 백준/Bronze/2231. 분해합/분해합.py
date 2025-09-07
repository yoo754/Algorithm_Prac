N =int(input())

for i in range(1, N+1):
  NN = list(map(int, str(i)))
  if sum(NN) + i == N:
    ans = ''.join(map(str, NN))
    print(ans)
    break
  if i == N:
    print(0)