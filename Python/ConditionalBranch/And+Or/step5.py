# 2 つの整数A、Bが与えられます。以下の条件を満たす場合はYESを、そうではない場合はNOを出力してください。
# ・「Aが 10 以上」 かつ 「Bが 10 以上ではない」

a,b = map(int,input().split())

if a >= 10 and not (b >= 10):
    print("YES")
else:
    print("NO")