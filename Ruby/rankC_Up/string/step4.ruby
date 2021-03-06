# 0 ~ 999 の整数 n が与えられます。 n が 3 桁の数である場合には n をそのまま出力し、 n が 2 桁の数である場合には n の先頭に 0 をひとつ、 1 桁の数である場合には n の先頭に 0 をふたつ加えたものを出力してください。

# 入力される値
# 入力は以下のフォーマットで与えられます。

# n

# 1 行目に整数 n が与えられます。

# n

# 期待する出力
# n を 3 桁で 0 埋めしたものを出力してください。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・0 ≤ n ≤ 999

number = gets.chomp
length = number.length

case length 
when 1
    puts "00" + number
when 2
    puts "0" + number
when 3
    puts number
end

# 回答例2
n = gets.to_i
p '%03d' % n
p format('%03d', n)
# %03d
# %・・・書式文字列であることを表す指示子
# 0・・・埋める文字。この場合ゼロ
# 3・・・桁数。この場合3桁
# d・・・出力する値の型。この場合整数(decimal)

# 回答例3
n = gets.chomp
answer = n.rjust(3, '0')
puts answer
