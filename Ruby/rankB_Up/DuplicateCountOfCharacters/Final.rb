# 1行目の文字が、2行目の文字列の中に何個出現するかをカウントして出力してください。

c = gets.chomp
s = gets.chomp

puts s.count(c)

# 回答例2
c = gets.chomp
s = gets.chomp
# 文字列を配列に分解
array = s.chars

i = 0
count = 0

s.length.times do
    if s[i] == c
        count += 1
    end
    i += 1
end

puts count