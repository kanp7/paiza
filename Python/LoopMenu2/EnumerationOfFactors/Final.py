# 整数 N が与えられます。
# N の約数を小さい方から順に改行区切りで出力してください。

n = int(input())

for i in range(1, n+1):
    if n % i == 0:
        print(i)