n, m, k = map(int, input().split())
mod = 998244353
dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    for j in range(1, m+1):
        for l in range(k-j+1):
            dp[i+1][l+j] = (dp[i+1][l+j]+dp[i][l])%mod
print(sum(dp[-1])%mod)