# 正の整数 N が与えられるので、1 〜 N の整数を 1 から順に半角スペース区切りで 1 行で出力してください。

n = int(input())
numbers = []
for i in range(n):
    numbers.append(str(i+1))
print(" ".join(numbers))
