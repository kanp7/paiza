# 0 ~ 9 の数字が 4 つ並んだ文字列 S が与えられます。
# 左から 1 番目の数と 4 番目の数を足し合わせたものを a とし、 2 番目の数と 3 番目の数を足し合わせたものを b とします。

# 文字列としての a の末尾に文字列としての b を結合したものを出力してください。


n = input()
a = int(n[0]) + int(n[3])
b = int(n[1]) + int(n[2])
print(str(a)+str(b))
