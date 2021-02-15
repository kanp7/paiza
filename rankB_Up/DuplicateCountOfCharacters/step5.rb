# 文字列 s が入力されるので、n 文字目と n + 1 文字目を出力してください。 n + 1 文字目がない場合は何も出力しないでください。

n = gets.chomp.to_i
str = gets.chomp

puts "#{str[n - 1]} #{str[n]}" if str[n]