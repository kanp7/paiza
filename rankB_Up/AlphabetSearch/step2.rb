# 英大文字の文字列が入力されます。
# この文字列の先頭1文字と末尾1文字で表される範囲に含まれる文字をすべて出力してください。

# 範囲とは、アルファベット順に並べた英大文字の列('A', 'B', 'C', ..., 'Z')について、先頭の文字の出現位置から末尾の文字の出現位置までの部分列のことです。
# たとえば、先頭の文字が'G'で末尾の文字が'O'で表される範囲は、('G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O')となります。

# 出力はアルファベット順に表示し、1文字表示するたびに改行してください。

word = gets.chomp

first = word[0]
last = word[-1]

output = (first..last).to_a
puts output