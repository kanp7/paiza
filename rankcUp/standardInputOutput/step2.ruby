# 入力される値
# 入力は以下のフォーマットで与えられます。

# n

# 整数 n が 1 行で与えられます。

# 入力値最終行の末尾に改行が１つ入ります。

# 期待する出力
# n 回 paiza と改行区切りで出力してください。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・1 ≦ n ≦ 50

input = gets.to_i
for num in 1..input do
  puts "paiza"
end