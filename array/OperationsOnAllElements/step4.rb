# 配列 A の要素数 N と配列 A の各要素である整数 A_1, A_2, ..., A_N が与えられるので、配列 A の要素の最小値 min を求めてください。

n = gets.to_i
numbers = []

n.times do
    numbers << gets.to_i
end

puts numbers.min