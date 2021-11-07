# A XOR B の結果を 0 または 1 で出力してください。末尾に改行を入れ、余計な文字、空行を含んではいけません。

a, b = map(int,input().split())

if a == b:
    print(0)
else:
    print(1)

# 解答2
a, b = map(int, input().split())
print(a ^ b)


# 解答3
def xor(x, y):
    return int((x and not y) or (not x and y))

a, b = map(int, input().split())
print(xor(a, b))
# AND 演算, OR 演算, NOT 演算のみで XOR 演算を表現する方法を実装します。
# 注意点として、 not 演算子は bool 型で計算されます。そのため、 xor 関数にて int 型で受け取った x , y は not 演算後に bool 型に変換されてしまいます。
# 問題文で 0 または 1 を出力するように指定されているので xor 関数では最後に、値を int 型に変換する必要があります。