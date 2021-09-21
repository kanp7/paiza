# n 個の数 a_1, ..., a_n が与えられます。与えられた数を大きい順に改行区切りで出力してください。

n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

num = sorted(num, reverse=True)
for i in num:
    print(i)


# 解答2
n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

a.sort(reverse=True)

for i in range(n):
    print(a[i])