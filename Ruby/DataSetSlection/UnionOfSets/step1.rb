# N 個の要素からなる数列Aと数値Bが与えられます。BがAに含まれているか判定してください。

n, b = gets.split(" ").map(&:to_i)
a = gets.chomp.split.map(&:to_i)

if a.include?(b)
    puts "Yes"
else
    puts "No"
end