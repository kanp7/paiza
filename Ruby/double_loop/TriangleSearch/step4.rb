# 整数 N が与えられるので、1 × 2 × ... × (N-1) × N を最大で何回 2 で割ることができるかを求めてください。

n = gets.to_i
count = 0

(1..n).each do |i|
    while i%2==0  do
        i = i/ 2 
        count += 1
    end
end

puts count