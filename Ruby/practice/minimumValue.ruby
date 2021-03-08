# 入力される値
# 入力は以下のフォーマットで与えられます。

# n_1
# n_2
# n_3
# n_4
# n_5

# ・1 行目から 5 行目に正の整数 n_1, n_2, n_3, n_4, n_5 が与えられます。

# 期待する出力
# n_1, n_2, n_3, n_4, n_5 のうち最も小さい数字を出力して下さい。

# 出力の最後に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・1 ≦ n_1, n_2, n_3, n_4, n_5 ≦ 100


n1 =gets.chomp.to_i
n2 =gets.chomp.to_i
n3 =gets.chomp.to_i
n4 =gets.chomp.to_i
n5 =gets.chomp.to_i

array = [n1, n2, n3, n4, n5]
puts array.min