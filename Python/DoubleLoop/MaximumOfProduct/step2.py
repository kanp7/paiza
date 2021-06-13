# 正の整数 N が与えられるので、1 〜 N の整数を 1 から順に改行区切りで N 行で出力してください。

n = int(input())
for i in range(n):
    print(i+1)
    i += 1