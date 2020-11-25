# 配列 A の要素数 N と配列 A の各要素である整数 A_1, A_2, ..., A_N が与えられるので、配列 A の要素の最大値 max を求めてください。

n = gets.to_i
array = []

n.times do
    array << gets.to_i
end

puts array.max