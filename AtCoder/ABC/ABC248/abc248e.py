n, k = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        (xi, yi), (xj, yj) = xy[i], xy[j]
        ver = []
        for l, (x, y) in enumerate(xy):
            if (xi-x)*(yj-y) == (xj-x)*(yi-y): ver.append(l)
        if len(ver) >= k and sorted(ver)[:2] == [i, j]: ans += 1
print(ans if k > 1 else "Infinity")