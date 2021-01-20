# 文字列 S が与えられるので、 S を整数に変換できる場合には "YES" , そうでない場合は "NO" を出力してください。

# なお、文字列 S を数値に変換できるとは、S の全ての文字が
# { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 } のいずれかであることをいいます。

n = gets.chomp
alp = ("a".."z").to_a + ("A".."Z").to_a

count = 0
alp.each do |a|
    if n.include?(a)
        puts "NO"
        break
    else
        count += 1
    end
end

if count == 52
    puts "YES"
end

# 回答例2
s = gets.chomp

# //この間が正規表現, ^行の先頭, $行の末尾, +直前の文字が1個以上連続する, [0-9]0~9の任意の文字 ,=~ マッチするか場合真を返す, !! 明示的にtrueを表示させる（なくてもOK)
if !! (s =~ /^[0-9]+$/)
    puts "YES"
else
    puts "NO"
end