n, p = map(int, input().split())
ans1 = [[0]*(3*n-1) for _ in range(n)]
ans2 = [[0]*(3*n-1) for _ in range(n)]
ans1[0][1] = 1
ans2[0][0] = 1
for i in range(1, n):
    for j in range(3*n-1):
        if j > 2: ans1[i][j] += ans1[i-1][j-3]+ans2[i-1][j-3]
        if j > 1: ans1[i][j] += ans1[i-1][j-2]*3
        if j > 1: ans2[i][j] += ans2[i-1][j-2]
        if j > 0: ans2[i][j] += ans1[i-1][j-1]*2
        ans1[i][j] %= p
        ans2[i][j] %= p
print(*ans1[-1][-2:-n-1:-1])