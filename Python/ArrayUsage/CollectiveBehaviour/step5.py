# 開店直後に店に入るために、番号 1 〜 N の N 人が開店前に店の前にブルーシートを合計 K 枚置きました。ブルーシートの先頭は A_1 , 最後尾は A_K です。しかし、店側は先頭から F 枚のブルーシートを撤去しました。

# 1 〜 N 番の人々は次のルールに従って店に並びます。
# ・自分のブルーシートが 1 枚以上残っているとき、自分のブルーシートのうち、最も先頭に近いブルーシートの位置に並ぶ。
# ・自分のブルーシートが 1 枚も残っていないとき、並ぶことなく帰宅する。

# 全員が並び終わった後に待機列にいる人の番号を先頭から順に答えてください。


n ,k, f = list(map(int,input().split())) 

nums = []
for _ in range(k):
    nums.append(int(input()))
del nums[:f]  # 最初からf番目まで

no_duplicate = []
for n in nums:
    if not n in no_duplicate:
        no_duplicate.append(n)
        print(n)


# 解答2
n, k, f = map(int, input().split())
a = [int(input()) for _ in range(k)]
a_removed = a[f:]  # f番目から最後まで
ans = []

for i in a_removed:
    if i not in ans:
        ans.append(i)
        print(i)