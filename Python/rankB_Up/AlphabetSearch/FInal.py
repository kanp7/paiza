# 1行目の英大文字 X から、2行目の英大文字 Y の範囲に3行目のアルファベット C が含まれていれば"true", そうでなければ"false"と出力してください。
# X が Y よりもアルファベット順で後ろになる場合(X = 'G', Y = 'F'のときなど)も"false"と出力してください。

x = input()
y = input()
c = input()

alp = ([chr(ord("A")+i) for i in range(26)])

x_i = (alp.index(x))
y_i = (alp.index(y))
c_i = (alp.index(c))

if c_i >= x_i and c_i <= y_i:
    print("true")
else:
    print("false")

