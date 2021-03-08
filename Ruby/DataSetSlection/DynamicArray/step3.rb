# 自然数A, B, Cが与えられます。(A, B, Cの最大値) - (A, B, Cの最小値)を答えてください。

array = gets.split.map(&:to_i)
puts array.max - array.min