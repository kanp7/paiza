# 2 つの整数A、Bが与えられます。AとBが両方とも 10 以上の場合はYESを、そうではない場合はNOを出力してください。

a,b = map(int, input().split())

if a >= 10 and b >= 10:
    print("YES")
else:
    print("NO")