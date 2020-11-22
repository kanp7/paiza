# 配列 A の要素数 N と整数 K, 配列 A の各要素 A_1, A_2, ..., A_N が与えられるので、配列 A に K がいくつ含まれるか数えてください。

n, k = gets.chomp.split(" ").map(&:to_i)
array = []
n.times do
    array << gets.to_i
end

puts array.count(k)
    