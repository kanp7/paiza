# スペース区切りの2つの整数が入力されるので、その区間の全ての整数を順に表示してください。

a, b = gets.chomp.split.map(&:to_i)
(a..b).each do |i|
    puts i
end
    