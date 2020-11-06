# 1行目の英大文字 X から、2行目の英大文字 Y の範囲に3行目のアルファベット C が含まれていれば"true", そうでなければ"false"と出力してください。
# X が Y よりもアルファベット順で後ろになる場合(X = 'G', Y = 'F'のときなど)も"false"と出力してください。

x = gets.chomp
y = gets.chomp
z = gets.chomp

array = ('A'..'Z').to_a

xi = array.index(x)
yi = array.index(y)
zi = array.index(z)

if zi <= yi && xi <= yi
    puts true
else
    puts false
end

# 回答例2
x = gets.chomp.ord
y = gets.chomp.ord
z = gets.chomp.ord

range = x..y

if y < x
  puts false
else
  puts range.include? z
end

# 回答例3
string = []
3.times do
  string.push(gets.chomp)
end

puts string[0].ord <= string[2].ord && string[2].ord <= string[1].ord