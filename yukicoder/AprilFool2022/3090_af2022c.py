n = int(input())
a = set()
for _ in range(n):
    v, w = map(int, input().split())
    a.add(w)
print("Yes" if 1 in a else "No")