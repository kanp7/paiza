# スペース区切りで2つの整数が入力されるので、その区間の整数を全て表示してください。

a, b = gets.split(" ").map(&:to_i)
range = a..b
range.each do |i|
    puts i
end
