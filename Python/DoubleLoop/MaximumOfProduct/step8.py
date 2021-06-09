# 整数 N , K と N 行 K 列 の二次元配列 A が与えられるので、 A の行ごとの和を出力してください。

n, k = list(map(int,input().split()))
for _ in range(n):
    num = list(map(int,input().split()))
    print(sum(num))