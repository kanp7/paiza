# 与えられる文字列の数 N と、 N 個の文字列が与えられるので、それらを順に末尾に連結した文字列を出力してください。

# 例として、"abc", "def", "ghi" という順で文字列が与えられたとき、連結後の文字列は"abcdefghi" となります。

n = gets.to_i

arrays = []

n.times do
    arrays << gets.chomp
end

puts arrays.join