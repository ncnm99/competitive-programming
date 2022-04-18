from math import isqrt
def count(n): return isqrt(n)+isqrt(n//2)
for _ in range(int(input())):
    l, r = map(int, input().split())
    print((count(r)-count(l-1))%2)