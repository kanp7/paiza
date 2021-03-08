# 1行目に行数を表す整数 n、続く n 行で m 個の「文字」と「整数」の組が空白区切りで入力されます。
# n 個の整数だけをそのまま順に出力してください。

n = gets.to_i

n.times do
    s, d = gets.chomp.split(" ")
    puts d
end

