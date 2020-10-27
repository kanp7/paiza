# 整数nが与えられるので、nが5以上なら"high"、そうでないなら"low"と出力してください。

n = gets.to_i

if n >= 5
    puts "high"
else
    puts "low"
end

# 回答例2
n = gets.to_i

puts n >= 5 ? "high" : "low"