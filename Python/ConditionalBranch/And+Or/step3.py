# 2 つの整数A、Bが与えられます。A, B の少なくとも一方が 10 以上の場合はYESを、そうではない場合はNOを出力してください。

a,b = map(int,input().split())

if a >= 10 or b >= 10:
    print("YES")
else:
    print("NO")