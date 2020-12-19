n = gets.to_i
count = 0

(1..n).each do |i|
    yakusuu = 0 
    (1..i).each do |j|
        if i%j == 0
            yakusuu += 1
        end
    end
    if yakusuu == 2
        count += 1
    end
end

puts count