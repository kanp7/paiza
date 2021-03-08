# 正整数 n と、 n 個の整数 a_1, ..., a_n が半角スペース区切りで与えられます。
# 与えられた整数の中に 3 の倍数がいくつあるかを数え、出力してください。

# 入力される値
# 入力は以下のフォーマットで与えられます。

# n
# a_1 a_2 ... a_n

# 1 行目に正整数 n が、 2 行目に n 個の整数 a_1, ..., a_n が半角スペース区切りで与えられます。

# 期待する出力
# 与えられた整数の中に3の倍数がいくつあるかを出力してください。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・n および各 a_i (1 ≤ i ≤ n） は 1 以上 50 以下の整数

n = gets.chomp.to_i
array = gets.chomp.split(" ").map(&:to_i)
odd_number = array.count{ |x| x % 3 == 0 }
puts odd_number

# 回答2
n = gets.to_i
array = gets.chomp.split(" ", n).map(&:to_i)

ans = 0

for num in array
  if num % 3 == 0
    ans += 1
  end
end

puts ans