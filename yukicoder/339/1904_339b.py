from collections import Counter
from math import factorial
n = int(input())
a = list(map(int, input().split()))
ans = factorial(n)
for m in Counter(a).values(): ans //= factorial(m)
print(ans)