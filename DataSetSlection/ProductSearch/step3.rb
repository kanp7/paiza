# 文字列がN個与えられます。各文字列の出現回数を文字列の辞書順で出力してください。

n = gets.to_i

strings = []
n.times do
    s = gets.chomp
    strings << s
end

list =  strings.group_by(&:itself).map{ |key, value| [key, value.count] }.to_h.sort

list.each do |key,value|
    puts key + " " + value.to_s
end