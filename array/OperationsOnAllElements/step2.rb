# 配列 A の要素数 N と配列 A の各要素 A_1, A_2, ..., A_N が整数として与えられるので、配列 A の全ての要素の和を求めてください。

n = gets.to_i

a = 0
n.times do
    i = gets.to_i
    a += i
end

puts a