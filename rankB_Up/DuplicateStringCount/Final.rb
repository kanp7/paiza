# 1行目で文字列 s、2行目で文字列 t が入力されます。
# s が t の中で何回出現するかカウントして出力してください。

s = gets.chomp
t = gets.chomp

number_of_split = t.length - s.length + 1
count = 0

number_of_split.times do |i|
    slice = t.slice(i,s.length)
    if slice == s
        count += 1
    end
end

puts count

# 補足
# s = "AA"
# t = "abdeeAAbAAAbfde"
# t.scan(s).lengthの場合
# AAAの部分が[0][1],[1][2]で判定されず回数が不足するためエラーとなる。
# 結果2, 答え3
