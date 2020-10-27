# 改行区切りで整数がn個入力されるので、n個の整数のうち、5以上のものを全て足し合わせた値を出力してください。

n = gets.to_i

sum = 0
n.times do
    a = gets.to_i
    if a >= 5
        sum += a
    end
end

puts sum