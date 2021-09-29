# 整数 n が与えられ、その後に n 個の整数 a_1, ..., a_n が半角スペース区切りで与えられるので、a_1, ..., a_n をそのままの順番で改行区切りで出力してください。


n = int(input())
num = map(int,input().split())
for n in num:
    print(n)