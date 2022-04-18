# [yukicoder contest 338](https://yukicoder.me/contests/375) 感想
ABE3完。Cも通したかった……。

## [A - Cycle](https://yukicoder.me/problems/no/1893)
答えは自明なのでどうすれば綺麗に書けるかを考える。いろいろ考えてみて、X,Y,Zをそれぞれ4で割った余りは等しいのでそれをrとするとX+Y+Z=12+3rになることに気付く。
```python=
x, y = map(int, input().split())
print(12+x%4*3-x-y)
```

## [B - Delete AB](https://yukicoder.me/problems/no/1894)
前から見ると、**AB**の後に**AA**が来ると残すべき、**B**が来ると消すべき、**AB**が来ると不明となり判断が付かないので、後ろから見るべきだと分かる。後ろを辞書順最大にしておけば、**AB**の後が**AB**になった時も残してよい。よって後ろから見て、**ABB**となった時に**AB**を消す、という操作を繰り返す。
```python=
for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = []
    for v in s[::-1]:
        ans.append(v)
        if len(ans) >= 3 and ans[-3:] == ["B", "B", "A"]:
            ans.pop(); ans.pop()
    print("".join(ans[::-1]))
```

## [C - Mod 2](https://yukicoder.me/problems/no/1895)
例えばx=a^3b^2cであるときf(x)=(a^0+a^1+a^2+a^3)(b^0+b^1+b^2)(c^0+c^1)となるので、xが2で何回割れてもf(x)の偶奇には関係なく、xの全ての奇素数が偶数乗であるとき、すなわちxが奇数の平方数に任意の回数2をかけたものであるとき、f(x)は奇数になる。
そこでf(x)が奇数になるものをあらかじめ全列挙してリストに入れて、クエリごとに二分探索して個数を求めようとしたが、max(R)が大きすぎるため間に合わない。改善策が思いつかず時間切れ。
解説を読む。前計算するのではなく、実装がやや面倒だがクエリごとに2で割れる回数で場合分けすれば解けたらしい。また、「奇数の平方数に任意の回数2をかけたもの」は「平方数または平方数の2倍」と言い換えられる。言われてみればそうだが、自力で気付くのは厳しかった。二分探索を用いなくとも平方根を切り捨てれば求められる。int(sqrt(x))をすると誤差で落ちるので、`math.isqrt`を使う。
```python=
from math import isqrt
def count(n): return isqrt(n)+isqrt(n//2)
for _ in range(int(input())):
    l, r = map(int, input().split())
    print((count(r)-count(l-1))%2)
```
ただし、`math.isqrt`は`Python 3.8`以降にしかないため、`PyPy`を使いたい場合は自力実装する必要がある。公式の実装とは異なるが以下の実装で通る。
```python=
def isqrt(n):
    m = int(n**0.5)
    if m*m > n: m -= 1
    if (m+1)**2 <= n: m += 1
    return m
```

## [E - Sum of 2nd Max](https://yukicoder.me/problems/no/1897)
まず、2番目ではなく1番目に大きな数を求めることを考える。1番目に大きな数がi(1\leq i\leq K)となる数列の数をf(i)とする。ある数列にiがj(1\leq j\leq N)個あるとすると、まずj個のiの位置を決めて、残りは1からi-1の中から独立に選べるので、二項定理より、
f(i)=\sum_{j=1}^N{}_NC_j(i-1)^{N-j}=\sum_{j=0}^N{}_NC_j(i-1)^{N-j}1^j-(i-1)^N=i^N-(i-1)^N
となる。要素の和を答えるのでiをかけるのを忘れないようにする。
実際に求めるのは1番目に大きな数ではなく2番目に大きな数なので、2番目に大きな数が1番目に大きな数と同じ時と異なる時に分けて考える。1番目に大きな数と同じ時は、iが最低2個必要なので、
f(i)=\sum_{j=2}^N{}_NC_j(i-1)^{N-j}=i^N-(i-1)^N-N(i-1)^{N-1}
となり、1番目に大きな数と異なる時は、1番目に大きな数は位置がN通りあり数はi+1からKの中から選べるので、
f(i)=N(K-i)\sum_{j=1}^{N-1}{}_{N-1}C_j(i-1)^{N-j}=N(K-i)(i^{N-1}-(i-1)^{N-1})
となる。
```python=
n, k = map(int, input().split())
mod = 998244353
ans = 0
for i in range(1, k+1):
    ans = (ans+i*(pow(i, n, mod)-pow(i-1, n, mod)-n*pow(i-1, n-1, mod)))%mod
    ans = (ans+i*n*(k-i)*(pow(i, n-1, mod)-pow(i-1, n-1, mod)))%mod
print(ans)
```