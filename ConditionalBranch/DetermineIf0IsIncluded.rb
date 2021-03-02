# 長さ N の数列Aが与えられます。Aの中に 0 が含まれていない場合はYESを、 0 が含まれている場合はNOを出力してください。

n = gets.to_i

numbers = []
n.times do 
    numbers << gets.to_i
end

if numbers.include?(0)
    puts "NO"
else
    puts "YES"
end

