# 指定した配列（リスト）を定義し、配列（リスト）の要素すべてを全て加算して出力してください。

array = [1, 3, 5, 6, 3, 2, 5, 23, 2]
puts array.sum

# 回答例2
array = [1, 3, 5, 6, 3, 2, 5, 23, 2]
array.inject(:+)

# 回答例3
array = [1, 3, 5, 6, 3, 2, 5, 23, 2]
answer = 0
array.each do |i|
    answer += i
end
puts answer