# 指定した配列（リスト）を定義し、それらの要素のうち5以上の数を全て足して結果を出力してください。

array = [ 4, 0, 5, -1, 3, 10, 6, -8 ]

sum = 0
array.each do |i|
    if i >= 5
        sum += i
    end
end

puts sum