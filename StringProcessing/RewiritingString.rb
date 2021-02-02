# 文字列 S と整数 i と文字 c が与えられるので、S の i 文字目を c に書き換えたものを出力してください。

s = gets.chomp
i, c = gets.chomp.split(" ")
i = i.to_i

s[i-1] = c

puts s