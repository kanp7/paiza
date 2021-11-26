# 1行目で整数 n が与えられ、2行目で n 個の整数が与えられます。
# n 個の整数を昇順に出力してください。

n = int(input())
for _ in range(n):
    s, d = input().split()
    print(d)