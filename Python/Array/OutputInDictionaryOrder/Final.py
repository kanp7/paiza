# 1 行目に整数 N, K が与えられます。
# 2 行目に N 個の文字列 s_1, s_2, ..., s_N が半角スペース区切りで与えられます。
# N 個の文字列を辞書順に並べ替え、K 番目の文字列を出力してください。

n, k = map(int,input().split())
numbers = sorted(input().split())
print(numbers[k-1])