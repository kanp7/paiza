# -1,000 ≦ A ≦ B ≦ 1,000 を満たす 2 つの整数 A, B が与えられます。A 以上 B 以下である 2 つの整数 X, Y を適当に選んだとき、X * Y の取り得る値の最小値を出力してください。なお、X と Y は同じ値でもよいものとします。
# たとえば A が 3, B が 5 の場合について考えます。これは X と Y を両方とも 3 にしたときが最小で、 X * Y が 9 となります。

a, b = map(int,input().split())

if a > 0 and b > 0:
    print(a*a)
elif a < 0 and b < 0:
    print(b*b)
else:
    print(a*b)