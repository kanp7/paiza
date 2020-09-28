# 入力される値
# 入力は以下のフォーマットで与えられます。

# a
# S

# 1 行目に文字 a が、 2 行目に文字列 S が与えられます。

# 期待する出力
# S に a が含まれている場合には “YES” を、そうでない場合には “NO” を出力してください。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・a, S はそれぞれ大文字または小文字のアルファベットからなる文字、文字列
# ・S の長さは 1 以上 10 以下

a = gets.chomp
s = gets.chomp

if s.include?(a)
    puts "YES"
else
    puts "NO"
end

# 回答例2
a = gets.chomp
s = gets.chomp
puts s.include?(a) ? "YES" : "NO"