# NOT A の結果を 0 または 1 で出力してください。末尾に改行を入れ、余計な文字、空行を含んではいけません。

a = int(input())

if a == 0:
    print(1)
else:
    print(0)


# 解答2
a = int(input())
# intでTrue,Falseを数値に変換
print(int(not a))
