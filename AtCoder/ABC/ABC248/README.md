# [AtCoder Beginner Contest 248(ユニークビジョンプログラミングコンテスト2022)](https://atcoder.jp/contests/abc248) 感想
E問題の誤差回避が上手くいかず$4$完。久しぶりの大爆死。

## [A - Lacked Number](https://atcoder.jp/contests/abc248/tasks/abc248_a)
各数字を$45$から引けばよい。A問題なので`for`文を使わなくても解けるがかなり面倒。
```python=
ans = 45
for v in input(): ans -= int(v)
print(ans)
```

## [B - Slimes](https://atcoder.jp/contests/abc248/tasks/abc248_b)
なんとなく`for`文で書こうとして上限をミスってWA。あまりにももったいない。素直に`while`文で書くべき。ちなみに答えの最大値は$2^{30}>10^9$より$30$。
言語によってはオーバーフローに気を付けないといけないらしい。大変ですね。
```python=
a, b, k = map(int, input().split())
i = 0
while a < b: i += 1; a *= k
print(i)
```

## [C - Dice Sum](https://atcoder.jp/contests/abc248/tasks/abc248_c)
まず二項係数で解けないかを考えたが、それぞれに$M$という上限があるので厳しい。よく見ると制約が小さいのでDPで解けそう。EDPCのどこかで見た累積和を取る必要があるやつかと一瞬思ったが、C問題でそんなものが出るはずないので落ち着いて計算量を考えると、愚直にやっても$O(NMK)$なので間に合う。実装にやや手間取ってしまった。精進が足りない。最近C問題やF問題にDPがかなり出ていて、実質EDPCみたいなところある。
以下の実装で、$dp[i][l]$は$i$番目まで見た時に和が$l$である場合の数。$j$は$i+1$番目の数。
解説を見ると、累積和を取ることも想定されていたみたい。それとは別に二項係数と包除原理を使って$O(K)$で解けるらしい。以前同様の問題を考えて分からなかった気がする。
```python=
n, m, k = map(int, input().split())
mod = 998244353
dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    for j in range(1, m+1):
        for l in range(k-j+1):
            dp[i+1][l+j] = (dp[i+1][l+j]+dp[i][l])%mod
print(sum(dp[-1])%mod)
```

## [D - Range Count Query](https://atcoder.jp/contests/abc248/tasks/abc248_d)
累積和やBITを使おうにも$O(N^2)$かからないかと一瞬思うも、愚直にやる場合と逆に考えて数字ごとにインデックスをメモしておくと、クエリは二分探索で$O(logN)$で答えられると気付く。リストや二分探索のインデックスに気を付けて実装する。
以下の実装の$a[i]$は、値が$i$であるものの数列$A$でのインデックスが1-indexedで入る。
Wavelet Matrixとかいう文字列を最近よく見るが、学習することをサボっている。
```python=
from bisect import bisect_right
n = int(input())
a = [[] for _ in range(n+1)]
for i, v in enumerate(map(int, input().split())): a[v].append(i+1)
for _ in range(int(input())):
    l, r, x = map(int, input().split())
    print(bisect_right(a[x], r)-bisect_right(a[x], l-1))
```

## [E - K-colinear Line](https://atcoder.jp/contests/abc248/tasks/abc248_e)
点を$2$つ選んで直線を作り、各点がその直線上にあるかを調べれば$O(N^3)$で解けることにはすぐ気が付いたが、重複して数えないように既に見た直線をどうやって保持するかで大苦戦。
傾きや切片は小数になるためそのまま`set`に入れると誤差で落ちる。誤差の出ない`Decimal`を使って無理やり通そうとするも、TLEだけでなく何故かWAも出てしまった。未だに謎。結果的には有理数を保持してくれる`Fraction`を使えば通ったのだが、以前別の問題で使ったときに`Decimal`より遅かったので使うことを避けてしまった。とりあえず試せばよかった。
以下の実装では$ans1$には傾きが$\infty$すなわち$Y$軸に平行な直線を、$ans2$にはそれ以外の直線を入れている。流れとしては、まず$2$点$i,j$を決め、その$2$点を通る直線の式を$y=ax+b$として$a,b$を求める。後は各頂点がその直線上にあるかを調べるわけだが、ここで直線の式に直接代入すると`Fraction`の計算がさすがに重すぎてTLEしたので、座標の差をたすき掛けして求める方法で調べた。
後から言われてみれば、確かに直線は$ax+by+c=0$($a,b,c$は整数)で書けるので、その方法でやる方がライブラリを使わずに済むし速いので良いが、実装が分からない。数学力……。
```python=
from fractions import Fraction
n, k = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(n)]
ans1, ans2 = set(), set()
for i in range(n-1):
    for j in range(i+1, n):
        (xi, yi), (xj, yj) = xy[i], xy[j]
        if xi == xj:
            if xi in ans1: continue
            count = 0
            for x, y in xy:
                if x == xi: count += 1
            if count >= k: ans1.add(xi)
        else:
            a = Fraction(yj-yi, xj-xi)
            b = Fraction(yi)-a*Fraction(xi)
            if (a, b) in ans2: continue
            count = 0
            for x, y in xy:
                if (xi-x)*(yj-y) == (xj-x)*(yi-y): count += 1
            if count >= k: ans2.add((a, b))
print(len(ans1)+len(ans2) if k > 1 else "Infinity")
```
以下の実装はコンテスト後にTwitterで見た解法。直線上の頂点を集めてソートして、最初の$2$点が決め打ちした$2$点だったときのみ答えに加算するというもの。これだと計算量が$O(N^3logN)$になっていてかつ同じ計算を何度もやっているが意外と速い。
他には直線上の頂点の組み合わせを全てチェックして、その組み合わせは以後見ないという方法があるらしい。これだと計算量は$O(N^3)$でかつ無駄な計算もしないので速そう。
```python=
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
```

## [F - Keep Connect](https://atcoder.jp/contests/abc248/tasks/abc248_f)
後日自力AC。各$i$について出力させる問題なので、$i$を増やしたり減らしたりしていく感じのDPができるのかと思いきやできそうにない。図を眺め左から順番に見ていけばいけそうだと気付く。後はいつものDPと同様に、辺の本数を保持して、今見ている位置の上下が連結の場合と非連結の場合で分けて遷移を考えればよい。左端の辺のみ別で考えて、後はコの字型で考える。
ある位置までで上下が連結の場合、￣または＿を追加すると非連結になり、￣｜か＿｜か￣＿か￣＿｜を追加すると連結のままになる。非連結の場合、￣＿を追加すると非連結のままになり、￣＿｜を追加すると連結になる。以下の実装では$ans1$が連結のものの数、$ans2$が非連結のものの数。
自力ACをした時は逆コの字型で考えて最後に右端の辺を付け加えることを考えた。遷移は似たような感じだが、上記のようなコの字型の方が実装がシンプルになる。
```python=
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
```