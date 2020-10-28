# スペース区切りの2つの整数が入力されるので、それらを足して出力してください。

a, b = gets.chomp.split(" ").map(&:to_i)
puts a + b