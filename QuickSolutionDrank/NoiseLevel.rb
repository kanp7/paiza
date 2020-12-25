# 騒音値は、デシベル（dB）という単位で表され、

# 騒音値の大きさで、騒音の大きさが判断されます。

# ~ 30 dB : 静か
# 30 ~ 50 dB : 普通
# 50 ~ 70 dB : うるさい
# 70 ~ dB : とてもうるさい


# 入力として騒音値（dB）が与えられるので、

# 騒音の大きさがどれほどであるのかを出力してください。


i = gets.to_i

if i < 30
    puts "quiet"
elsif i >= 30 && i < 50
    puts "normal"
elsif i >= 50 && i <70
    puts "noisy"
else
    puts "very noisy"
end