# 長さ N の重複した要素の無い数列 A と整数 K が与えられるので、
# A に K が含まれていれば "YES" を、そうでなければ "NO" を出力してください。

n, k = list(map(int,input().split()))

l = []
for _ in range(n):
    l.append(int(input()))

if k in l:
    print("YES")
else:
    print("NO")