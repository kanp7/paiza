# 1行目で正の整数nが入力され、続くn行の各行で整数が1つずつ入力されます。n個の整数を小さい順に改行区切りで出力してください。

# 入力される値
# 入力は以下のフォーマットで与えられます。

# n (数字の総数)
# a_1
# a_2
# a_3
# ...
# a_i
# ...
# a_n

# 期待する出力
# 入力された正の整数a_iを小さい順に改行区切りで出力してください。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# 1 ≦ n ≦ 100
# 1 ≦ i ≦ nについて、1 ≦ a_i ≦ 1000

n = gets.to_i
array = []
n.times do
    number = gets.to_i
    array << number
end

sortNumber = array.sort

puts sortNumber