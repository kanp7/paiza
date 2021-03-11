# 整数Xが与えられます。Xが 10 以上ではない場合はYESを、Xが 10 以上である場合はNOを出力してください。

x = int(input())
if not (x >= 10):
    print("YES")
else:
    print("NO")