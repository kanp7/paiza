# 文字列 S が与えられるので、 S が回文かどうかを判定してください。
# なお、回文とは、前から読んでも後ろから読んでも同じ文字列になるような文字列のことをいいます。

n = gets.chomp

if n == n.reverse
    puts "YES"
else
    puts "NO"
end