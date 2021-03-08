n = gets.chomp.to_i

array = []
n.times do
    a = gets.chomp.to_i
    array << a
end

flag = 0
for num in array
    if num == 7
        flag = 1
    endfor
end

if flag == 1
    puts "YES"
else
    puts "NO"
end

# 回答２
n = gets.to_i
a = n.times.map{gets.to_i}

if a.any? { |t| t == 7 }
  puts "YES"
else
  puts "NO"
end