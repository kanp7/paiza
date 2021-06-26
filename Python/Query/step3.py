# 長さ N の重複した要素の無い数列 A と Q 個の整数 K_1 ... K_Q が与えられるので、
# 各 K_i について、 A に K_i が含まれていれば "YES" を、そうでなければ "NO" を出力してください。

n, q = list(map(int,input().split()))

numbers = []
for _ in range(n):
    numbers.append(int(input()))

for _ in range(q):
    k = int(input())
    if k in numbers:
        print("YES")
    else:
        print("NO")

# n=98765 q=100000 のとき時間切れ