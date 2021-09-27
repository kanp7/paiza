# 文字 a と文字列 S が与えられるので、 S に a が含まれているかどうか判定し、含まれている場合には “YES” を、そうでない場合には “NO” を出力してください。

a = input()
s = input()

if a in s:
    print("YES")
else:
    print("NO")