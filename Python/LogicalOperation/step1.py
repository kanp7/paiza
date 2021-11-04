# 0 または 1 の整数 A と B が与えられます。 A AND B の結果を出力してください。


a,b = map(int,input().split())
if a == 1 and b == 1:
    print(1)
else:
    print(0)


# 解答2
a, b = map(int, input().split())

print(a and b)