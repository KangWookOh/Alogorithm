import sys
input = sys.stdin.readline

N , K  = map(int, input().split())
items = []

for _ in range(N):
    W , V = map(int,input().split())
    items.append((W,V))


dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for w in range(1,K+1):
        if items[i-1][0] <= w:
            dp[i][w] = max(items[i-1][1]+dp[i-1][w-items[i-1][0]],dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]
print(dp[N][K])