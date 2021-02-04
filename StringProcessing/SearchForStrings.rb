# 文字列 S , T が与えられるので、 T が S の部分文字列かどうかを判定してください。
# なお、 S の部分文字列とは、 S の連続した 1 文字以上を取り出してできる文字列のことです。

s = gets.chomp
t = gets.chomp

if s.include?(t)
    puts "YES"
else
    puts "NO"
end

