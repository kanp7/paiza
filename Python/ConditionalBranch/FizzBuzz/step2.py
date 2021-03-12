# 整数Nが与えられます。Nが 3 の倍数かつ 5 の倍数の場合はYESを、そうではない場合はNOを出力してください。

n = int(input())

if n % 15 == 0:
    print("YES")
else:
    print("NO")
