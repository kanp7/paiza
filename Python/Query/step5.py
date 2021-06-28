# 数列 A と入力の回数 K が与えられるので、K 回の入力に応じて次のような処理をしてください。
# ・pop
# A の先頭の要素を削除する。既に A に要素が存在しない場合何もしない。
# ・show
# A の要素を先頭から順に改行区切りで出力する。A に要素が存在しない場合何も出力しない。

n, k = list(map(int,input().split()))

nums = []
for _ in range(n):
    nums.append(int(input()))

for _ in range(k):
    query = input()
    if query == "pop":
        nums.pop(0)
    elif query == "show":
        for n in nums:
            print(n)
