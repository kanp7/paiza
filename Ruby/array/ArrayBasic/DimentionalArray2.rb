# 1 行目に整数 N, M, K, L が与えられます。
# 2 行目以降に N 行 M 列の二次元配列が与えられます。
# 配列の K 行目 L 列目の要素を出力してください。
# 上から i 番目、左から j 番目の整数は a_ij です。

n,m,k,l = gets.split(" ").map(&:to_i)

arrays = []

n.times do 
    arrays << gets.split(" ").map(&:to_i)
end

puts arrays[k-1][l-1]