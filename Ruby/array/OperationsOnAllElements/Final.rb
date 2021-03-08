# 配列 A の要素数 N と整数 K, 配列 A の各要素 A_1, A_2, ..., A_N が与えられるので、配列 A の全ての要素を + K した後の A の各要素を出力してください。

n, k = gets.chomp.split(" ").map(&:to_i)

n.times do 
    i = gets.to_i
    puts i + k
end