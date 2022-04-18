n, m = map(int, input().split())
ans = [1]*n
for _ in range(m):
    p, q, a, b = map(int, input().split())
    if a < 0 or b < 0: ans = [-1]
print(*ans)