# 数値 N が入力されます。1 から N までの数値をすべて、改行区切りで出力してください。

n = gets.to_i

(1..n).each do |i|
    puts i
end