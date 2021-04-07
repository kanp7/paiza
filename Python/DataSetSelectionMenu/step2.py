# 要素数Nの数列Aと要素数Qの数列B与えられます。 1 ≦ i ≦ Q の各iについて、i行目には以下の数値を出力してください
# * AのB_i番目の値を出力してください。

n = int(input())
list_a = list(map(int,input().split()))
q = int(input())
list_b = list(map(int,input().split()))

for i in list_b:
    print(list_a[i-1])
