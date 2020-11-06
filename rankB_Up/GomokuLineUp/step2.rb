# 1行5列の五目並べの盤面が与えられます。

# 盤面の各マスには、"O"か"X"か"."が書かれています。

# "O"と"X"は、それぞれプレイヤーの記号を表します。

# 同じ記号が横に連続で5つ並んでいれば、その記号のプレイヤーが勝者となります。

# 勝者の記号を1行で表示してください。
# 勝者がいない場合は、引き分けとして、"D"を表示してください。

# 不正解
s = gets.chomp.chars

o = 0
x = 0
5.times do |i|
    if s[i] == "O"
        o += 1
    else s[i] == "X"
        x += 1
    end
end

if o == 5
    puts "O"
elsif x == 5
    puts "X"
else
    puts "D"
end

# 回答例2
array = ['O', 'X']
string = gets.chomp.split('')
result = 'D'

array.each do |a|
  cnt = 0
  string.each do |s|
    if s == a
      cnt = cnt + 1
    end
  end
  if cnt >= 5
    result = a
  end
end
puts result