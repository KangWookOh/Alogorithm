def max_profit(N,schedule):
    dp =[0]*(N+1)
    max_profit = 0

    for i in range(N):
        max_profit = max(max_profit,dp[i])
        if i + schedule[i][0] <= N :
            dp[i+ schedule[i][0]] = max(dp[i+schedule[i][0]],max_profit+schedule[i][1])
    return max(dp)

N = int(input())
schedule = [list(map(int,input().split())) for _ in range(N)]

print(max_profit(N,schedule))