# スペース区切りの2つの整数と、文字列が入力されるので、2つの整数の範囲の部分文字列を出力してください。

n = gets.split(" ")
a = n[0].to_i - 1
b = n[1].to_i - 1

s = gets.chomp

puts s[a..b]

回答例2
n = gets.split(" ")
a = n[0].to_i - 1
b = n[1].to_i - 1

s = gets.chomp

puts s.slice(a..b)