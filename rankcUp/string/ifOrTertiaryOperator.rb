# 5行の入力が与えられます。

# ・1行目では整数aが与えられます。aが0より大きいなら"plus"、そうでなければそのまま1行目で表示してください。
# ・2行目では文字列bが与えられます。bが"hoge"に一致するなら"yes"、そうでなければそのまま2行目で表示してください。
# ・3行目では文字列cが与えられます。cが10文字なら"ten"、そうでなければそのまま3行目で表示してください。
# ・4行目では文字列dが与えられます。dが文字"x"を含むなら"x"が最初に見つかった位置、そうでなければ"nothing"を4行目で表示してください。
# ・5行目では文字列eが与えられます。eが5文字なら"five"、そうでなければeの最初の1文字だけを5行目で表示してください。

# 入力される値
# 5行の各行でa,b,c,d,eが与えられます。

# 期待する出力
# 適切な5行の出力してください。

a = gets.to_i
puts a > 0 ? "plus" : a

b = gets.chomp
puts b == "hoge" ? "yes" : b

c = gets.chomp
puts c.length == 10 ? "ten" : c

d = gets.chomp
if d.include?("x") 
    puts d.index("x")
else
    puts "nothing"
end

e = gets.chomp
puts e.length == 5 ? "five" :e[0]
