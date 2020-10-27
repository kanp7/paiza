# n 人の人の名前 s_1, ..., s_n が与えられたのち、 m 回の「攻撃」に関する情報が与えられます。各行は “p_i a_i” というフォーマットで与えられ、 p_i はダメージを受けた人の名前 （s_1, ..., s_n のいずれか） 、 a_i は p_i が受けたダメージ数を表す数です。

# 最後に人名 S が与えられるので （S は s_1, ..., s_n のいずれか） 、 S が受けたダメージの合計を出力してください。なお、一度もダメージを受けていない人の合計ダメージは 0 とします。

# 入力される値
# 入力は以下のフォーマットで与えられます。

# n
# s_1
# ...
# s_n
# m
# p_1 a_1
# ...
# p_m a_m
# S

# 1 行目には正整数 n が与えられ、 2 行目から (n + 1) 行目には人の名前 s_1, ..., s_n が改行区切りで与えられます。 (n + 2) 行目には正整数 m が与えられ、 (n + 3) 行目から (n + m + 2) 行目には人の名前 p_i （s_1, ..., s_n のいずれか） とその人が受けたダメージ a_i が "p_i a_i" という半角スペース区切りのフォーマットで m 行与えられます。 (n + m + 3) 行目には s_1, ..., s_n の中のいずれかの人名 S が与えられます。

# 期待する出力
# S の受けた合計ダメージを出力してください。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・1 ≤ n, a_i ≤ 50 （1 ≤ i ≤ n）
# ・各 s_i （1 ≤ i ≤ n） は大小アルファベットからなる長さ 1 以上 10 以下の文字列で、互いに全て異なる

n = gets.to_i
s = n.times.map{gets.chomp}

m = gets.to_i
arrays = m.times.map{gets.chomp.split(" ", 2)}

array_to_i = []
arrays.each{|array| array_to_i << [array[0], array[1].to_i]}
hash =  array_to_i.group_by(&:first).map{|k, v| [k, v.sum(&:last)]}.to_h
# array_to_i.group_by(&:first)で→の状態にする {"Kyoko"=>[["Kyoko", 1], ["Kyoko", 2]]}

key_word = gets.chomp

if hash.key?(key_word)
  ans =  hash.fetch_values(key_word)
  puts ans
else
  ans = 0
  puts ans
end

# 別回答
n = gets.to_i
characters = {}
n.times do
    characters[gets.strip] = 0
end
​
m = gets.to_i
m.times do
    char, damage = gets.split(' ')
    characters[char] += damage.to_i
end
​
puts characters[gets.strip]