# 整数 N, K, Q と、 長さ N の配列 A_1, A_2, ..., A_N が与えられるので、A_K の後ろに Q を挿入した後の長さ N+1 の配列について、先頭から改行区切りで出力してください。

n, k ,q = list(map(int,input().split()))

lists = []
for _ in range(n):
    lists.append(int(input()))

lists.insert(k, q)

for x in lists:
    print(x)