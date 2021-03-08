# 配列 A と B についての情報が与えられるので、(A の 1 つの要素) × (B の 1 つの要素) の最大値を求めてください。

n, k = gets.chomp.split(" ").map(&:to_i)
array1 = gets.chomp.split(" ").map(&:to_i)
array2 = gets.chomp.split(" ").map(&:to_i)
ans = []
array1.each do |n|
    array2.each do |m|
        ans << n * m
    end
end
puts ans.max

# 回答例2
len_a, len_b = gets.chomp.split(' ').map(&:to_i)
​
A = gets.chomp.split(' ').map(&:to_i)
B = gets.chomp.split(' ').map(&:to_i)
​
a_min, a_max = A.min, A.max
b_min, b_max = B.min, B.max
​
​
puts [a_min * b_min, a_max * b_min, a_min * b_max, a_max * b_max].max

# 回答例3
len_a, len_b = gets.chomp.split(' ').map(&:to_i)
​
A = gets.chomp.split(' ').map(&:to_i)
B = gets.chomp.split(' ').map(&:to_i)
​
# maximum = 0 だと積の結果の最大値がマイナスの場合、product > maximum の判定がうまく行かない
maximum = nil
​
A.each do |a|
    B.each do |b|
        product = a * b
        if maximum.nil? or product > maximum
            maximum = product
        end
    end
end
​
puts maximum