# [yukicoder contest 339](https://yukicoder.me/contests/376) 感想
2完。厳しい……。

## [A - Day1](https://yukicoder.me/problems/no/1903)
素直な問題設定で好き。7日目からは7日で1問減らせる。Nが小さい時に気を付ける。
```python=
n = int(input())
print((n-6)*7+6 if n > 6 else n)
```

## [B - Never giving up!](https://yukicoder.me/problems/no/1904)
回数の期待値と聞いて身構えるも、単純な試行なのでゲームの成功確率の逆数でよい。ゲームで失敗になるタイミングが様々なので難しそうに感じるが、順列を考えて広義単調増加になっている確率を考えれば問題ない。Aから作ることのできる広義単調増加の順列の並び自体は1通りしかなく、そのような並びになる場合の数は、`1 2 2 3 3 3`であれば1!*2!*3!といったように、それぞれの個数の階乗を掛け合わせたものになる。求めるものは成功確率の逆数なので、これで全体のN!を割ればよい。
不思議なことに、求める式や答えはAから作ることのできる順列の場合の数と等しくなる。何故だろう。
```python=
from collections import Counter
from math import factorial
n = int(input())
a = list(map(int, input().split()))
ans = factorial(n)
for m in Counter(a).values(): ans //= factorial(m)
print(ans)
```

## [C - PURE PHRASE](https://yukicoder.me/problems/no/1905)
ヒューリスティックコンテストのような問題だと感じた。各周期の最大値のタイミングを記録して、その間隔の平均を取ればよいだろうと思い、全体の最大値との差が一定以下のものを選んだり、全体の最大値より少し小さいものより大きなものを選んだりしたが、余計なものが紛れ込んでしまったのかWAがちらほら出てしまった。
解説を読んだ。確かに今回は解の候補が分かっているのだから、それぞれの場合の当てはまり具合を計算して最も良いものを選べばよかった。数学や統計学的にはよろしくないと思われるが、当てはまり具合は素直に差の絶対値の和で実装した。
物理を知らないのでフーリエ変換は分からない。
```python=
n = int(input())
a = list(map(int, input().split()))
height = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]
freq = [261.6, 294.3, 327.0, 348.8, 392.4, 436.0, 490.5]
period = [round(n/v) for v in freq]
diff = [0]*7
for i, v in enumerate(period):
    for j in range(n-v): diff[i] += abs(a[j]-a[j+v])
print(height[diff.index(min(diff))])
```