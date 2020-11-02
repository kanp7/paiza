s = gets.chomp
t = gets.chomp

number_of_split = t.length - s.length + 1
count = 0

number_of_split.times do |i|
    slice = t.slice(i,s.length)
    if slice == s
        count += 1
    end
end

puts count