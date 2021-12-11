# 1行目に行数を表す整数 n、続く n 行で n 個の「文字」と「整数」の組が空白区切りで入力されます。
# n 個の整数だけをそのまま順に出力してください。

n = int(input())
for _ in range(n):
    s, d = input().split()
    print(d)
