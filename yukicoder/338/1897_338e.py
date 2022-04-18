n, k = map(int, input().split())
mod = 998244353
ans = 0
for i in range(1, k+1):
    ans = (ans+i*(pow(i, n, mod)-pow(i-1, n, mod)-n*pow(i-1, n-1, mod)))%mod
    ans = (ans+i*n*(k-i)*(pow(i, n-1, mod)-pow(i-1, n-1, mod)))%mod
print(ans)