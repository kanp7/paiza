# 1 行目に整数 N が与えられます。
# N 番目までのフィボナッチ数を出力してください。

# フィボナッチ数は

# F_0 = 0
# F_1 = 1
# F_(n+2) = F_n + F_(n+1) (n は 0 以上)

# とし、F_0 を 1 個目とします。

n = gets.to_i

numbers = [0,1]

n.times do |i|
    if i > 1
        numbers << numbers[i-2] + numbers[i-1]
    end
end

puts numbers