n = gets.to_i

array = gets.split.map(&:to_i)

ans = []

(0..9).each do |i|
    count = 0
    array.each do |j|
        if i == j
            count += 1
        end
    end
    ans << count 
end

puts ans.join(" ")
