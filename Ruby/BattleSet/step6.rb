# 英語の名前が与えられたとき、その名前をイニシャルに変換するシステムを作ることにしました。

# 「ファーストネーム ラストネーム」で与えられる半角アルファベットの氏名をイニシャルで表してください。

f_name, l_name = gets.chomp.split(" ").map(&:capitalize)

puts  "#{f_name[0]}.#{l_name[0]}."