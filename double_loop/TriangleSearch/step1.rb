# N 行 K 列の行列 A の i 行 j 列 の要素 A_ij を A_ji とした K 行 N 列の行列を元の配列 A の転置行列と言います。

# 例として、

# 1 2 3
# 4 5 6
# 7 8 9

# の転置行列は

# 1 4 7
# 2 5 8
# 3 6 9

# 行列 A についての情報が与えられるので、A の転置行列を出力してください。
# N 行 K 列の行列 A の i 行 j 列 の要素 A_ij を A_ji とした K 行 N 列の行列を元の配列 A の転置行列と言います。

n, k = gets.split.map(&:to_i)

array = []
n.times do 
    array << gets.chomp.split.map(&:to_i)
end

transpose_of_matrix = []
k.times do |j|
    temp = []
    n.times do |i|
        temp << array[i][j]
    end
    transpose_of_matrix << temp
end

transpose_of_matrix.each do |t|
    puts t.join(" ")
end

# 回答例2
n, k = gets.split.map(&:to_i)

array = []
n.times do 
    array << gets.chomp.split.map(&:to_i)
end

ans = []
k.times do |i|
    temp = []
    array.each do |a|
        temp << a[i]
    end
    ans << temp.join(" ")
end
puts ans