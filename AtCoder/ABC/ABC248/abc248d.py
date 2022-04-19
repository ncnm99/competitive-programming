from bisect import bisect_right
n = int(input())
a = [[] for _ in range(n+1)]
for i, v in enumerate(map(int, input().split())): a[v].append(i+1)
for _ in range(int(input())):
    l, r, x = map(int, input().split())
    print(bisect_right(a[x], r)-bisect_right(a[x], l-1))