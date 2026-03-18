# 2579 계단 오르기
N = int(input())
stair = []
stair.append(0)
for i in range(1, N+1) :
  stair.append(int(input()))
dp = [0] * (N+1)

# 각 층에 올 수 있는 가장 큰 값을 저장
for i in range(1, N+1):
  dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i])

print(dp[N])