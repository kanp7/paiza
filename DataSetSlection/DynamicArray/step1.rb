# 要素数Nの数列Aと数値Mが与えられます。AのM番目の値を出力してください。

n,m = gets.split.map(&:to_i)
a = gets.split.map(&:to_i)

puts a[m-1]