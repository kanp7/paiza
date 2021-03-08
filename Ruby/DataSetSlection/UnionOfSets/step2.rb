# N 個の要素からなる数列Aが与えられます。数列Aは昇順にソートされています。Aの重複した要素を取り除いて昇順に出力してください。

n = gets.to_i
array = gets.chomp.split.map(&:to_i)

puts array.uniq.join(" ")