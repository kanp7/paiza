# 生徒の身長が A_1, ...., A_N であるような N 人のクラスで二人三脚の代表を決めることにしました。代表には、身長の差が最も小さいような 2 人を選出することにしました。選ばれた 2 人の身長を昇順に出力してください。

# 条件
# ・2 ≦ N ≦ 100
# ・100 ≦ A_i ≦ 200 (1 ≦ i ≦ N)
# ・代表となるようなペアは 1 組に限られることが保証されています。

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))
sorted_array = sorted(array)
# print(sorted_array) [102, 119, 132, 187, 191]

ans = abs(sorted_array[0] - sorted_array[1])
pair = []

for i in range(len(sorted_array)):
    if i > 0:
        subtract = abs(sorted_array[i]- sorted_array[i-1]) # 整列した配列の差を評価する。
        if subtract < ans:
            ans = subtract
            if len(pair) > 0:
                pair.clear()
            pair.extend([sorted_array[i], sorted_array[i-1]])

for j in (sorted(pair)):
    print(j)


# 解答2
n = int(input())
a = [int(input()) for _ in range(n)]
ans = [None, None]
diff = 101  # 与えられる身長の条件が100 ~ 200のため、必ず101以下の値で更新される 

for i in range(n):
    for j in range(i + 1, n):  # i以降の数字 ~ n(リストの数)でループ
        if abs(a[i] - a[j]) < diff:
            diff = abs(a[i] - a[j])
            ans = [a[i], a[j]]

ans.sort()
for i in ans:
    print(i)