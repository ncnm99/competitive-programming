# [yukicoder April Fool Contest 2022](https://yukicoder.me/contests/378) 感想
プログラミングコンテストに参加したら謎解きをさせられました。どうして……。ACの2完。
以下ネタバレ注意。

## [A - ACL list](https://yukicoder.me/problems/no/3088)
出力例をよく見ると3行目からは2行ずつセットになっているので、それらをまとめて出力すればよい。文字列のコピーが大変。以下のコードで171点。他の人の提出を見るともう少し短くできるらしい。
解説を読むともっと強い方法があるらしい。
```python=
print("LICENSE");print("all")
for v in ("convolution","dsu","fenwicktree","internal_bit","internal_csr","internal_math","internal_queue","internal_scc","internal_type_traits","lazysegtree","math","maxflow","mincostflow","modint","scc","segtree","string","twosat"):print(v);print(v+".hpp")
```

## [B - 32xtm fwf8ggk pgmer@ qr@,wsvb guf@t^xd@](https://yukicoder.me/problems/no/3089)
問題文が57577だがひらがなにしても何も分からない。ふと問題名を見ると57577に近い文字数になっていて、余分な文字っぽい@をふとキーボードでさがすと「゛」が書いてあり、かな入力だと気づく。
「あふさかも　はてはゆききの　せきもいず　たずねてとひこ　きなばかへさじ」と読めたはいいものの、教養が無くこれが実在する短歌だと気づけず詰まってしまい、解説AC。素直に検索すればよかったみたい。「沓冠折句」は国語の授業で扱ったような記憶がある。
```python=
print(int(input())*17)
```

## [C - Knapsack Function](https://yukicoder.me/problems/no/3090)
初め「同じ品物を複数回選んでもよい。」という条件を見逃しており、nが大きい時自明に-1ではと思ってしまう。その後条件を見つけるも、どんな入力でも逆にnが小さいときに-1になり得ると思い、`print("No")`を出力してWA。
よく考えると重さが1の品物がある時に単調増加になる。ない時はf(0)=0,f(1)=-1より単調増加にならない。
```python=
n = int(input())
a = set()
for _ in range(n):
    v, w = map(int, input().split())
    a.add(w)
print("Yes" if 1 in a else "No")
```

## [D - 3-2-SAT](https://yukicoder.me/problems/no/3092)
まんまと引っかかった。2-SATの解き方を知らなかったので調べて、上手いこと改造すればこの問題も解けそうだなと思っているうちに時間切れ。解説を読んでびっくり。かなり面白い問題だと思う。
```python=
n, m = map(int, input().split())
ans = [1]*n
for _ in range(m):
    p, q, a, b = map(int, input().split())
    if a < 0 or b < 0: ans = [-1]
print(*ans)
```