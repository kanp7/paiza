# 人事のあなたは、N 人の中から採用者を決定します。N 人のテストの点数はそれぞれ A_i (1 ≦ i ≦ N)です。テストの点数が K 点以上の人全員を採用したいのですが、得点の高い方から M 人に辞退されてしまいました。あなたの採用することのできる最大の人数を答えてください。採用できる人数が 0 人の場合もあることに気をつけてください。

# ランタイムエラー
n, k, m = map(int,input().split())

nums = []
for _ in range(n):
    point = int(input())
    if point >= k:
        nums.append(point)

nums = sorted(nums)

for _ in range(m):
    nums.pop()
print(len(nums))


# 解答2
n, k, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = 0

for i in a:
    if i >= k:
        ans += 1
ans -= m
if ans < 0:
    ans = 0

print(ans)