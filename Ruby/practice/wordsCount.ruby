# スペースで区切られた英単語列が与えられます。
# 英単語列に含まれる英単語の出現回数を出現した順番に出力してください。

# 入力される値
# 半角スペースで区切られた長さNの文字列

# 期待する出力
# 単語、半角スペース、出現回数の順で１行に１単語で出現したすべての単語を、列に出現する順に出力してください。

# 条件
# 全てのテストケースにおいて以下の条件を満たします。

# 1 ≦ N ≦ 1,000

strings = gets.chomp.split(" ")
hashs = strings.group_by(&:itself).map{ |key, value| [key, value.count] }.to_h
hashs.each do |key, value|
    puts "#{key} #{value}"
end