# 英大文字の文字列が入力されます。
# 文字列の先頭1文字が、末尾1文字よりもアルファベット順で先に出現するならば、"true"を出力し、そうでなければ"false"を出力してください。

word = gets.chomp
first, last = word[0], word[-1]

alp = ("A".."Z").to_a
first_idx = alp.index(first)
last_idx = alp.index(last)

if first_idx < last_idx
    puts "true"
else
    puts "false"
end

