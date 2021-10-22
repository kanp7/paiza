# 長さ N の数列 a (a_1, a_2, ..., a_N) と b (b_1, b_2, ..., b_N) が与えられます。
# a の各要素から b の各要素を引いた結果 (a_1 - b_1, a_2 - b_2, ..., a_N - b_N) を、改行区切りで出力してください。

n = int(input())
al = list(map(int,input().split()))
bl = list(map(int,input().split()))

for i in range(n):
    print(al[i]-bl[i])