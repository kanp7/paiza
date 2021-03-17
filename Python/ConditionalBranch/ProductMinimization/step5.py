# 2 以上の整数N, Kが与えられます。
# 「Nを 2 倍した数でNを更新する」という操作を何度か繰り返すことを考えます。
# このとき, ちょうどある回数 M で N の値は K 以上になります。この時点で操作の繰り返しを終了することにします。

# この繰り返しの回数Mを求めてください。(Mは 0 でも構いません)

# 例えば、Nを 2 、Kを 18 とします。
# 上記の操作を 3 回繰り返すと、N = 16 となります。
# 4 回くりかえすと、N = 32 となり、N >= K が成立します。ここで操作を終了し、最終的な操作の回数Mは 4 となります。

n,k = map(int,input().split())

count = 0
while n < k:
    n = n * 2
    count += 1

print(count)
