# N 個の要素からなる数列A, Bが与えられます。 AまたはBに含まれる値をすべて列挙し、昇順に出力してください。ただし出力する数列は重複した要素を取り除いてください。

n = gets.to_i

a = gets.split.map(&:to_i)
b = gets.split.map(&:to_i)
c = a.push(*b).uniq.sort

puts c.join(" ")

# 回答例２
c = a.concat(b).uniq.sort

# 回答例3
c = a.push(b)
# [1, 2, 3, [3, 4, 5]]
c = c.flatten.uniq.sort

puts c.join(" ")
