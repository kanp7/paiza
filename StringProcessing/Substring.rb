# 文字列 S と整数 i , j が与えられるので、 S の i 文字目から j 文字目までの部分文字列を出力してください。

s = gets.chomp
i,j = gets.split(" ").map(&:to_i)

puts s.slice(i-1..j-1)