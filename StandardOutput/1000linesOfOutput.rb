# 1 以上 1,000 以下の整数を昇順で、すべて改行区切りで出力してください。

(1..1000).each do |i|
  puts i
end

# 回答例2
i = 0
1000.times do 
    i += 1
    puts i
end