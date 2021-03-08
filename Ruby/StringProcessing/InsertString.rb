# 文字列 S , T と、整数 N が与えられるので、 S の N 文字目の後ろに T を挿入した文字列を出力してください。

s = gets.chomp
t = gets.chomp
n = gets.to_i

puts s.insert(n,t)