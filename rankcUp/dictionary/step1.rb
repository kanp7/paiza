# n 人の人に関して、それぞれの人の名前と財産が与えられます。その後に人名 S が与えられるので （S は最初に与えられた名前のうちのいずれか） 、 S の財産を表す整数を出力してください。

# 入力される値
# 入力は以下のフォーマットで与えられます。

# n
# s_1 a_1
# ...
# s_n a_n
# S

# 1 行目には正整数nが与えられ、 2 行目から (n + 1) 行目には、人々の名前と財産が “s_i a_i” というフォーマット （s_i は人の名前を表す文字列、 a_i はその人の財産を表す整数、半角スペース区切り）で与えられます。 (n + 2) 行目には人名 S が与えられます (S は 2 行目から (n + 1) 行目にかけて与えられた人名のいずれか）。

# 期待する出力
# S の財産を出力してください。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・1 ≤ n , a_i ≤ 50 （1 ≤ i ≤ n）
# ・各 s_i （1 ≤ i ≤ n） および S は大小アルファベットからなる長さ 1 以上 10 以下の文字

n = gets.to_i
array = []

n.times do
    array << gets.chomp.split(" ")
end

hash = Hash[*array.flatten]
# hash = array.to_h 上記と同じ
# {"Kirishima"=>"1", "Kyoko"=>"2"}

target_value = gets.chomp
puts hash[target_value].to_i

# 回答2
n = gets.to_i
hash = {}

n.times do
    value_key = gets.chomp.split(" ")
    # 1回目["Kirishima", "1"], 2回目["Kyoko", "2"]
    hash[value_key[0]] = value_key[1].to_i
    # 1回目{"Kirishima"=>1}, 2回目{"Kirishima"=>1, "Kyoko"=>2}
end

target_value = gets.chomp
# "Kirishima"

puts hash[target_value]
# 1


