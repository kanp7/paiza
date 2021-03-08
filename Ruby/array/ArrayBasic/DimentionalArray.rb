# 1 行目に整数 N と整数 K が与えられます。
# 2 行目に N 個の整数 a_i (1 ≤ i ≤ N) が半角スペース区切りで与えられます。
# a_i の K 番目の要素を出力してください。

n,k = gets.split(" ").map(&:to_i)
numbers = gets.split.map(&:to_i)

puts numbers[k-1]